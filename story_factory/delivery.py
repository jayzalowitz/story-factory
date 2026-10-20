#!/usr/bin/env python3
"""Prepare the selected, inspected local delivery. This never sends or publishes files."""
import argparse
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import shutil
from story_check import build_problems, quality_problems, truth_problems, selected_sources, draft_fingerprint
from package_options import load, output_names


def visual_problems(root):
    path=root/'development/visual_review.json'
    if not path.is_file():return ['Missing visual review: inspect the actual PDFs and record development/visual_review.json']
    try:data=json.loads(path.read_text())
    except (ValueError,OSError):return ['Invalid visual review JSON']
    if not isinstance(data,dict):return ['Visual review must be an object']
    records=data.get('outputs',{})
    if not isinstance(records,dict):return ['Visual review outputs must be an object']
    build=json.loads((root/'development/build.json').read_text())
    errors=[]
    for name in output_names(load(root)):
        filename=name+'.pdf';record=records.get(filename,{})
        actual=build.get('outputs',{}).get(filename,{})
        if not isinstance(record,dict):errors.append(f'Invalid visual record: {filename}');continue
        if record.get('sha256')!=actual.get('sha256'):errors.append(f'Visual review is missing or stale: {filename}')
        pages=actual.get('pages',0)
        if not isinstance(pages,int) or pages<1 or record.get('pages_inspected')!=list(range(1,pages+1)):
            errors.append(f'Inspect every delivered page: {filename}')
        if record.get('verdict')!='PASS' or not record.get('observations'):
            errors.append(f'Visual review needs observations and a passing verdict: {filename}')
    return errors


def prepare(root, destination=None):
    root=Path(root).resolve()
    errors=build_problems(root)+quality_problems(root)+truth_problems(root,require_draft=True)
    if not errors:errors+=visual_problems(root)
    if (root/'adaptation/project.json').exists():
        from adaptation import problems
        errors+=problems(root,final=True)
    if errors:raise ValueError('\n'.join(errors))
    destination=Path(destination) if destination else root/'delivery'/datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%S%fZ')
    destination=destination.resolve()
    if destination.exists():raise ValueError('Delivery destination must not exist; preserve the earlier delivery')
    if destination==root or root.is_relative_to(destination):raise ValueError('Delivery cannot contain the source project')
    sources=selected_sources(root)|{root/'Makefile',root/'latexmkrc'}
    sources.update(p for p in (root/'fonts').rglob('*') if p.is_file())
    for path in sources:
        if (not path.resolve().is_relative_to(root) or 'private' in path.resolve().relative_to(root).parts
            or any(parent.is_symlink() for parent in [path, *path.parents] if parent==root or root in parent.parents)):
            raise ValueError('Private or external print input requires a separate reviewed delivery decision')
    destination.mkdir(parents=True)
    build=json.loads((root/'development/build.json').read_text())
    manifest={'schema':1,'created':datetime.now(timezone.utc).isoformat(),'draft_sha256':draft_fingerprint(root),
              'selection':load(root),'review_status':'current editorial, truth and all-page visual receipts checked',
              'limitations':(root/'development/handoff.md').read_text() if (root/'development/handoff.md').is_file() else 'Read project reviews for creative and factual limitations; no professional certification.',
              'files':{}}
    try:
        for name in output_names(load(root)):
            filename=name+'.pdf';target=destination/'pdfs'/filename;target.parent.mkdir(exist_ok=True)
            shutil.copyfile(root/'output'/filename,target)
            manifest['files']['pdfs/'+filename]=build['outputs'][filename]
        options=load(root)
        if options['sections']:
            from package_options import package_entry
            wrapper=package_entry(root,options,write=True)
        else:wrapper=None
        for source in sorted(sources):
            relative=source.relative_to(root);target=destination/'editable'/relative;target.parent.mkdir(parents=True,exist_ok=True)
            if source==root/'package/studio_package.tex' and wrapper:
                target.write_bytes(wrapper.read_bytes())
            else:shutil.copyfile(source,target)
            manifest['files']['editable/'+relative.as_posix()]={'sha256':hashlib.sha256(target.read_bytes()).hexdigest()}
        (destination/'manifest.json').write_text(json.dumps(manifest,indent=2)+'\n')
        (destination/'READ_ME.txt').write_text('Your selected PDFs are in pdfs/. Editable print sources are in editable/.\nSee manifest.json for measured pages, review status and remaining limitations.\nTo rebuild exactly these files, ask your assistant to open editable/ and run:\nmake -B '+ ' '.join('output/'+name+'.pdf' for name in output_names(options))+'\nThese files have not been submitted, sent or published. Keep a backup.\n')
    except Exception:
        shutil.rmtree(destination)
        raise
    return destination


def main():
    parser=argparse.ArgumentParser(description=__doc__);parser.add_argument('--project',type=Path,default=Path(__file__).resolve().parents[1]);parser.add_argument('--destination',type=Path)
    args=parser.parse_args()
    try:print(prepare(args.project,args.destination))
    except (ValueError,OSError) as exc:parser.exit(1,str(exc)+'\n')

if __name__=='__main__':main()
