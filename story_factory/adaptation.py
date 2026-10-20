#!/usr/bin/env python3
"""Validate adaptation evidence and review currency; never judge fidelity automatically."""
import argparse
import hashlib
import json
from pathlib import Path

RIGHTS = {'user-owned', 'permission-recorded', 'public-domain-asserted', 'unresolved'}
KINDS = {'novel','memoir','article','play','oral-history','podcast','short-story','nonfiction','other'}

def sha(path): return hashlib.sha256(path.read_bytes()).hexdigest()

def local_file(root, name):
    if not isinstance(name,str) or not name or Path(name).is_absolute(): raise ValueError('Source paths must be project-relative')
    candidate=root/name
    if any(p.is_symlink() for p in [candidate,*candidate.parents] if p!=root.parent): raise ValueError('Source paths cannot use symlinks')
    resolved=candidate.resolve()
    if not resolved.is_relative_to(root.resolve()) or not resolved.is_file(): raise ValueError('Source file is missing or outside the project')
    return resolved

def fingerprint(root):
    paths=sorted(p for p in (root/'screenplay').rglob('*') if p.is_file() and p.suffix in {'.tex','.fountain','.md','.txt'})
    h=hashlib.sha256()
    for p in paths: h.update(p.relative_to(root).as_posix().encode()+b'\0'+p.read_bytes()+b'\0')
    return h.hexdigest()

def load(root):
    data=json.loads((root/'adaptation/project.json').read_text())
    if not isinstance(data,dict) or data.get('version')!=1: raise ValueError('Unsupported adaptation record version')
    return data

def problems(root, final=False):
    root=Path(root).resolve();errors=[]
    try: data=load(root)
    except (ValueError,OSError) as exc:return [f'Cannot read adaptation record: {exc}']
    if not isinstance(data,dict):return ['Adaptation record must be an object']
    sources=data.get('sources',[])
    if not isinstance(sources,list) or not sources:return ['Adaptation needs at least one source']
    known={}; source_hashes={}
    for source in sources:
        if not isinstance(source,dict):errors.append('Source must be an object');continue
        sid=source.get('id')
        if not isinstance(sid,str) or not sid or sid in known:errors.append('Source IDs must be unique nonempty strings');continue
        known[sid]=source
        if not isinstance(source.get('kind'),str) or source.get('kind') not in KINDS:errors.append(f'{sid}: unknown source kind')
        for key in ('title','provenance','locator_scheme'):
            if not isinstance(source.get(key),str) or not source[key].strip():errors.append(f'{sid}: missing {key}')
        rights=source.get('rights',{})
        if not isinstance(rights,dict) or not isinstance(rights.get('status'),str) or rights.get('status') not in RIGHTS or not rights.get('basis'):errors.append(f'{sid}: record source-use status and its basis')
        elif final and rights['status']=='unresolved':errors.append(f'{sid}: source-use question remains unresolved')
        try:
            p=local_file(root,source.get('path'));source_hashes[sid]=sha(p)
            if source.get('sha256')!=source_hashes[sid]:errors.append(f'{sid}: source changed; reread and update coverage')
        except (ValueError,OSError) as exc:errors.append(f'{sid}: {exc}')
        total=source.get('units');coverage=source.get('read_units',[])
        if type(total)!=int or total<1:errors.append(f'{sid}: units must be a positive integer');continue
        if not isinstance(coverage,list) or any(type(i)!=int or i<1 or i>total for i in coverage) or len(set(coverage))!=len(coverage):errors.append(f'{sid}: invalid read-unit coverage')
        elif final and set(coverage)!=set(range(1,total+1)):errors.append(f'{sid}: source has unread units')
    contract=data.get('contract',{})
    if not isinstance(contract,dict) or not contract.get('preserve') or not contract.get('change_policy') or not contract.get('scope'):errors.append('Fidelity contract needs scope, preserve list, and change policy')
    elif final and contract.get('status')!='approved':errors.append('Writer has not approved the fidelity contract')
    departures=data.get('departures',[])
    if not isinstance(departures,list):errors.append('Departures must be a list');departures=[]
    ids=set()
    for item in departures:
        if not isinstance(item,dict) or not isinstance(item.get('id'),str) or not item.get('id') or item.get('id') in ids:errors.append('Departure IDs must be unique');continue
        ids.add(item['id'])
        if not item.get('description') or not item.get('reason'):errors.append(f"{item['id']}: explain departure and purpose")
        if final and item.get('decision')!='approved':errors.append(f"{item['id']}: departure is not approved")
    scenes=data.get('scenes',[])
    if not isinstance(scenes,list):errors.append('Scenes must be a list');scenes=[]
    mapped=set()
    for scene in scenes:
        if not isinstance(scene,dict) or not isinstance(scene.get('id'),str) or not scene.get('id') or scene.get('id') in mapped:errors.append('Scene IDs must be unique');continue
        mapped.add(scene['id'])
        if not scene.get('transformation'):errors.append(f"{scene['id']}: explain cinematic transformation")
        refs=scene.get('source_refs',[])
        if not isinstance(refs,list):errors.append(f"{scene['id']}: source_refs must be a list");refs=[]
        if not refs and not scene.get('invention_reason'):errors.append(f"{scene['id']}: cite a source location or explain invention")
        for ref in refs:
            if not isinstance(ref,dict) or not isinstance(ref.get('source_id'),str) or ref.get('source_id') not in known or not ref.get('locator'):errors.append(f"{scene['id']}: invalid source reference")
        if not isinstance(scene.get('departure_ids',[]),list) or any(not isinstance(d,str) or d not in ids for d in scene.get('departure_ids',[])):errors.append(f"{scene['id']}: unknown departure ID")
    if final:
        import re
        actual=set()
        for p in (root/'screenplay').rglob('*'):
            if p.is_file() and p.suffix in {'.tex','.fountain','.md','.txt'}:actual.update(re.findall(r'(?:%|#|//)\s*scene:\s*([\w-]+)',p.read_text()))
        if not actual:errors.append('Add stable scene markers, for example % scene: S001, to the screenplay')
        if actual!=mapped:errors.append('Scene map does not match current screenplay scene markers')
        try:
            review=json.loads((root/'adaptation/review.json').read_text())
            if not isinstance(review,dict):raise ValueError('Review must be an object')
            if review.get('draft_sha256')!=fingerprint(root):errors.append('Adaptation review is stale for the screenplay')
            if review.get('record_sha256')!=sha(root/'adaptation/project.json'):errors.append('Adaptation review is stale for the source map/contract')
            if review.get('source_sha256')!=source_hashes:errors.append('Adaptation review is stale for source files')
            if review.get('coverage')!='full-draft' or review.get('verdict')!='READY' or not review.get('summary'):errors.append('Full-draft adaptation review requires revision')
        except (ValueError,OSError):errors.append('Missing or invalid adaptation/review.json')
    return errors

def main():
    parser=argparse.ArgumentParser(description='Check source reading, adaptation decisions, and review currency. This is not a legal or artistic verdict.')
    parser.add_argument('action',choices=['check','current','fingerprint']);parser.add_argument('--project',type=Path,default=Path.cwd())
    args=parser.parse_args();root=args.project.resolve()
    if args.action=='fingerprint':print(fingerprint(root));return 0
    errors=problems(root,args.action=='current')
    print('\n'.join(errors) if errors else 'Adaptation records are consistent' + (' and the review is current.' if args.action=='current' else '; this does not certify a finished adaptation.'))
    return 1 if errors else 0
if __name__=='__main__':raise SystemExit(main())
