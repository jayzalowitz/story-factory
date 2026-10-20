#!/usr/bin/env python3
"""Mechanical story checks. Editorial verdicts come from the writer and agent."""
import argparse
import hashlib
import json
from pathlib import Path
import re
import shutil
import subprocess
try:
    from package_options import load, output_names, package_entry, SECTIONS
except ModuleNotFoundError:
    from story_factory.package_options import load, output_names, package_entry, SECTIONS

ROOT = Path(__file__).resolve().parents[1]
PITCHES = ['one-pager','actor-pitch','director-pitch','financier-pitch','producer-pitch','distributor-pitch','streamer-pitch','festival-pitch','awards-pitch','coproduction-pitch','public-funder-pitch','talent-rep-pitch','exhibitor-pitch','cultural-partnership-pitch','press-pitch','craft-pitch']
MARKERS = re.compile(r'DRAFT PLACEHOLDER|TO BE (?:PROVIDED|DEVELOPED|WRITTEN)|\bTODO\b|\bTBD\b', re.I)


def digest(paths, root):
    h=hashlib.sha256()
    for p in sorted(paths):
        h.update(p.relative_to(root).as_posix().encode());h.update(b'\0');h.update(p.read_bytes());h.update(b'\0')
    return h.hexdigest()


def draft_fingerprint(root):
    return digest(list((root/'screenplay').rglob('*.tex')),root)


def selected_sources(root):
    root=root.resolve()
    options=load(root)
    paths=set()
    if options['screenplay']:paths.add(root/'screenplay/main_screenplay.tex')
    if options['sections']:
        paths.add(root/'package/studio_package.tex')
        paths.update(root/'package'/f'{name}.tex' for name in options['sections'])
    paths.update(root/'one_pagers'/f'{name}.tex' for name in options['pitches'])
    pending=list(paths)
    while pending:
        path=pending.pop()
        if not path.is_file():continue
        text=path.read_text()
        if path==root/'package/studio_package.tex' and options['sections']!=SECTIONS:
            if '% Package sections' not in text:raise ValueError('Studio wrapper needs its % Package sections marker')
            text=text.split('% Package sections',1)[0]
        text='\n'.join(line for line in text.splitlines() if not line.lstrip().startswith('%'))
        for target in re.findall(r'\\input\{([^}]+)\}',text):
            candidate=path.parent/target
            if not candidate.suffix:candidate=candidate.with_suffix('.tex')
            candidate=candidate.resolve()
            if candidate not in paths:paths.add(candidate);pending.append(candidate)
    return paths


def print_fingerprint(root):
    root=root.resolve()
    paths=selected_sources(root)
    paths.update(p for p in (root/'fonts').rglob('*') if p.is_file())
    paths.update([root/'Makefile',root/'latexmkrc'])
    if (root/'development/package_options.json').exists():paths.add(root/'development/package_options.json')
    return digest(paths,root)


def source_problems(root):
    root=root.resolve()
    options=load(root);errors=[]
    for path in sorted(selected_sources(root)):
        if not path.is_file():errors.append(f'Missing deliverable source or input: {path.relative_to(root)}');continue
        text=path.read_text()
        if path==root/'package/studio_package.tex' and options['sections']!=SECTIONS:
            text=text.split('% Package sections',1)[0]
        text='\n'.join(line for line in text.splitlines() if not line.lstrip().startswith('%'))
        if MARKERS.search(text):errors.append(f'Unwritten content: {path.relative_to(root)}')
    return errors


def quality_problems(root):
    errors=[]
    fingerprint=draft_fingerprint(root)
    reports={}
    for name in ['quality','bechdel']:
        path=root/f'development/{name}.json'
        if not path.is_file(): errors.append(f'Missing review receipt: {path.relative_to(root)}');continue
        try:report=json.loads(path.read_text())
        except (ValueError,OSError):errors.append(f'Invalid JSON: {path.relative_to(root)}');continue
        reports[name]=report
        if report.get('draft_sha256')!=fingerprint:errors.append(f'Stale {name} review; review the current screenplay')
        if report.get('coverage')!='full-draft':errors.append(f'{name} report does not cover the full draft')
        if not report.get('summary'):errors.append(f'{name} report needs an evidence summary')
    quality=reports.get('quality',{})
    if quality and quality.get('verdict')!='READY':errors.append('Quality review still requires revision')
    bechdel=reports.get('bechdel',{})
    if bechdel:
        status=bechdel.get('status')
        if status not in ['PASS','FAIL','UNCLEAR']:errors.append('Bechdel report must say PASS, FAIL, or UNCLEAR')
        if status=='PASS' and not any(len({name.strip() for name in e.get('women',[]) if isinstance(name,str) and name.strip()})>=2 and e.get('scene_id') and e.get('exchange') and e.get('non_man_topic') for e in bechdel.get('evidence',[])):
            errors.append('Bechdel PASS needs two named women, an actual exchange, scene ID, and non-man topic')
        prefs=root/'development/preferences.json'
        target=json.loads(prefs.read_text()).get('bechdel_target','report') if prefs.exists() else 'report'
        if target=='pass' and status!='PASS':errors.append('Writer requested a Bechdel pass; current result does not meet that target')
    return errors


def truth_problems(root, require_draft=False):
    path=root/'research/source_mode.json'
    if not path.exists():return []
    errors=[]
    try:mode=json.loads(path.read_text()).get('mode')
    except ValueError:return ['Invalid research/source_mode.json']
    if mode not in ['original','based-on','inspired-by']:return ['Unknown source mode']
    if mode=='original':return []
    ledger=root/'research/claims.json'
    if not ledger.exists():return ['Missing research/claims.json']
    try:data=json.loads(ledger.read_text())
    except ValueError:return ['Invalid research/claims.json']
    sources={s.get('id'):s for s in data.get('sources',[])}
    claims=data.get('claims',[])
    if not claims:errors.append('True-story mode needs a researched claim ledger')
    seen=set()
    for claim in claims:
        identity=claim.get('id')
        if not identity or identity in seen:errors.append('Claim IDs must be nonempty and unique')
        seen.add(identity)
        if claim.get('status') not in ['verified','disputed','unverified','inference','invented']:errors.append(f'{identity}: unknown evidence status')
        for sid in claim.get('source_ids',[]):
            if sid not in sources:errors.append(f'{identity}: missing source {sid}')
        if claim.get('status')=='verified':
            cited=[sources[sid] for sid in claim.get('source_ids',[]) if sid in sources]
            if not cited:errors.append(f'{identity}: verified claim has no source')
            for source in cited:
                if not all(source.get(k) for k in ['url','title','accessed','locator']) or 'example.invalid' in source.get('url',''):
                    errors.append(f'{identity}: source lacks usable citation details')
    report=root/'research/truth_report.md'
    if not report.exists():errors.append('Missing research/truth_report.md; source consistency is not truth verification')
    if require_draft:
        receipt=root/'research/truth.json'
        if not receipt.exists():errors.append('Missing full-draft research/truth.json receipt')
        else:
            result=json.loads(receipt.read_text())
            if result.get('draft_sha256')!=draft_fingerprint(root):errors.append('Truth review is stale for this screenplay')
            if result.get('claims_sha256')!=hashlib.sha256(ledger.read_bytes()).hexdigest():errors.append('Truth review is stale for the claim ledger')
            if result.get('verdict')!='READY':errors.append('Truth review requires revision')
    return errors


def output_limit_problems(root, outputs):
    prefs=root/'development/preferences.json'
    if not prefs.is_file():return []
    data=json.loads(prefs.read_text())
    if not isinstance(data,dict):return ['development/preferences.json must be an object']
    limit=data.get('screenplay_max_pages')
    if limit is None or 'screenplay.pdf' not in outputs:return []
    if type(limit) is not int or not 1 <= limit <= 1000:return ['screenplay_max_pages must be an integer from 1 to 1000 or null']
    record=outputs.get('screenplay.pdf')
    if record and (type(record.get('pages')) is not int or record['pages']>limit):
        return [f"Screenplay exceeds the writer's {limit}-page physical PDF limit; revise layout/content honestly, never pad or shrink unreadably"]
    return []


def build_problems(root):
    root=root.resolve()
    path=root/'development/build.json'
    if not path.exists():return ['No build receipt; run story_check.py build']
    data=json.loads(path.read_text())
    errors=[]
    if data.get('source_sha256')!=print_fingerprint(root):errors.append('Print sources changed since the build')
    expected={name+'.pdf' for name in output_names(load(root))}
    if set(data.get('outputs',{}))!=expected:errors.append('Build receipt does not match selected documents')
    for name in output_names(load(root)):
        record=data.get('outputs',{}).get(name+'.pdf',{})
        path=root/'output'/f'{name}.pdf'
        if not path.exists() or hashlib.sha256(path.read_bytes()).hexdigest()!=record.get('sha256'):
            errors.append(f'Missing or changed PDF: {name}')
        if name in PITCHES and record.get('pages')!=1:errors.append(f'{name} is not one page')
    return errors+output_limit_problems(root,data.get('outputs',{}))


def build(root):
    root=root.resolve()
    errors=source_problems(root)
    if errors:raise ValueError('\n'.join(errors))
    if not shutil.which('pdfinfo'):raise ValueError('Install pdfinfo to measure the actual PDFs; no page counts were invented.')
    options=load(root)
    entry=package_entry(root,options,write=True)
    before=print_fingerprint(root)
    targets=['output/'+name+'.pdf' for name in output_names(options)]
    command=['make','-B']+targets
    if entry:command.append('PACKAGE_ENTRY='+entry.name)
    subprocess.run(command,cwd=root,check=True)
    outputs={}
    for name in output_names(load(root)):
        path=root/'output'/f'{name}.pdf'
        info=subprocess.check_output(['pdfinfo',str(path)],text=True)
        count=int(re.search(r'^Pages:\s+(\d+)',info,re.M).group(1))
        if name in PITCHES and count!=1:raise ValueError(f'{name}: expected 1 page, got {count}')
        outputs[path.name]={'pages':count,'sha256':hashlib.sha256(path.read_bytes()).hexdigest()}
    limits=output_limit_problems(root,outputs)
    if limits:raise ValueError('\n'.join(limits))
    if print_fingerprint(root)!=before:raise ValueError('Sources changed during build; rerun against stable files')
    (root/'development').mkdir(exist_ok=True)
    (root/'development/build.json').write_text(json.dumps({'source_sha256':before,'outputs':outputs},indent=2)+'\n')
    print(f'Built and measured {len(outputs)} selected PDFs. Visual inspection and editorial review still required.')


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('command',choices=['fingerprint','source','quality','truth','truth-current','build','check-build'])
    parser.add_argument('--project',type=Path,default=ROOT)
    args=parser.parse_args();root=args.project.resolve()
    try:
        if args.command=='fingerprint':print(draft_fingerprint(root));return
        if args.command=='build':build(root);return
        functions={'source':source_problems,'quality':quality_problems,'truth':truth_problems,'truth-current':lambda root: truth_problems(root,require_draft=True),'check-build':build_problems}
        problems=functions[args.command](root)
        if problems:raise ValueError('\n'.join(problems))
        print(f'{args.command}: mechanical checks passed; not an artistic or legal certification.')
    except (ValueError,OSError,KeyError,subprocess.CalledProcessError) as error:
        parser.exit(1,f'{error}\n')


if __name__=='__main__':main()
