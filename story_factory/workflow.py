#!/usr/bin/env python3
"""Track evidence and stale work in the Story Factory writing workflow."""
import argparse
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import re
from story_check import quality_problems, truth_problems, build_problems
from package_options import load as package_options

ROOT=Path(__file__).resolve().parents[1]
STAGES={
 'discover':(['development/brief.md','development/discovery.md'],'development/discovery.md'),
 'research':(['research/plan.md','research/report.md','research/claims.json','research/truth_report.md'],'research/report.md'),
 'premise':(['development/story_bible.md','development/premise_review.md'],'development/premise_review.md'),
 'structure':(['development/outline.md','development/scene_map.md','development/continuity.md','development/structure_review.md'],'development/structure_review.md'),
 'draft':(['screenplay/**/*.tex','development/draft_report.md'],'development/draft_report.md'),
 'revise':(['development/review.md','development/revision_log.md','development/quality_report.md','development/bechdel_report.md','development/quality.json','development/bechdel.json'],'development/review.md'),
 'package':(['package/*.tex','one_pagers/*.tex','development/package_review.md'],'development/package_review.md'),
 'verify':(['development/verification.md','development/build.json','common/*.tex','Makefile','latexmkrc'],'development/verification.md'),
 'handoff':(['README.md','development/status.md','development/handoff.md'],'development/handoff.md'),
}
COMMANDS={'discover':'story-office-hours','research':'story-research','premise':'story-premise','structure':'story-outline','draft':'story-draft','revise':'story-revise','package':'story-package','verify':'story-check','handoff':'story-handoff'}
MARKERS=re.compile(r'DRAFT PLACEHOLDER|TO BE (?:PROVIDED|DEVELOPED|WRITTEN)|\bTODO\b|\bTBD\b',re.I)


def source_mode():
 path=ROOT/'research/source_mode.json'
 mode=json.loads(path.read_text()).get('mode') if path.exists() else 'original'
 if mode not in ['original','based-on','inspired-by']:raise ValueError('Invalid source mode; use original, based-on, or inspired-by')
 return mode


def active_stages():
 return [stage for stage in STAGES if stage!='research' or source_mode()!='original']


def artifacts(stage):
 files={};problems=[]
 patterns=list(STAGES[stage][0])
 if stage=='package':
  options=package_options(ROOT)
  patterns=['development/package_review.md']
  if options['sections']:patterns+=['package/studio_package.tex']+[f'package/{name}.tex' for name in options['sections']]
  patterns += [f'one_pagers/{name}.tex' for name in options['pitches']]
  if (ROOT/'development/package_options.json').exists():patterns.append('development/package_options.json')
 if stage=='discover':
  for name in ['research/source_mode.json','development/preferences.json']:
   if (ROOT/name).exists():patterns.append(name)
 for pattern in patterns:
  matches=sorted(ROOT.glob(pattern))
  if not matches:problems.append(f'Missing: {pattern}')
  for path in matches:
   name=path.relative_to(ROOT).as_posix();content=path.read_text()
   prose='\n'.join(line for line in content.splitlines() if not line.lstrip().startswith('%'))
   if path.suffix!='.json' and (len(prose.strip())<80 or MARKERS.search(prose)):problems.append(f'Incomplete or placeholder: {name}')
   if path.suffix=='.json':json.loads(content)
   files[name]=hashlib.sha256(path.read_bytes()).hexdigest()
 report=ROOT/STAGES[stage][1]
 if report.exists() and not re.search(r'^Verdict:\s*PASS\s*$',report.read_text(),re.M):problems.append(f'Review must explicitly record Verdict: PASS: {report.relative_to(ROOT)}')
 if stage=='research':
  problems+=truth_problems(ROOT)
  truth=ROOT/'research/truth_report.md'
  if truth.exists() and not re.search(r'^Verdict:\s*PASS\s*$',truth.read_text(),re.M):problems.append('Research truth review needs a truthful PASS or more research')
 if stage in ['revise','verify']:problems+=quality_problems(ROOT)
 if stage=='verify':problems+=truth_problems(ROOT,require_draft=True)+build_problems(ROOT)
 return files,problems


def current(receipts):
 for stage in active_stages():
  if stage not in receipts:return stage,False
  files,problems=artifacts(stage)
  if problems or files!=receipts[stage]['files']:return stage,True
 return None,False


def save(receipts):
 state=ROOT/'development/workflow.json';state.parent.mkdir(parents=True,exist_ok=True)
 temporary=state.with_suffix('.tmp')
 temporary.write_text(json.dumps({'schema':2,'completed':receipts},indent=2)+'\n');temporary.replace(state)


def main():
 parser=argparse.ArgumentParser(description=__doc__);sub=parser.add_subparsers(dest='command',required=True)
 sub.add_parser('status');sub.add_parser('check')
 complete=sub.add_parser('complete');complete.add_argument('stage',choices=STAGES);complete.add_argument('--evidence',required=True)
 reopen=sub.add_parser('reopen');reopen.add_argument('stage',choices=STAGES);reopen.add_argument('--reason',required=True)
 args=parser.parse_args()
 try:
  state=ROOT/'development/workflow.json';receipts=json.loads(state.read_text())['completed'] if state.exists() else {}
  stage,stale=current(receipts);order=active_stages()
  if args.command in ['status','check']:
   for name in STAGES:
    if name not in order:print(f'{name}: not required for original fiction');continue
    label='complete' if name in receipts else 'pending'
    if name==stage:label='STALE; reopen required' if stale else 'NEXT'
    elif stage and order.index(name)>order.index(stage) and name in receipts:label='pending revalidation'
    print(f'{name}: {label}')
   if stage:print(f'Next: /{COMMANDS[stage]} (Claude) or ${COMMANDS[stage]} (Codex). Read WORKFLOW.md.')
   if args.command=='check' and stage:
    _,problems=artifacts(stage);print('\n'.join(problems) if problems else 'Artifacts present; creative judgment still required.')
    raise SystemExit(1 if stale or problems else 0)
   return
  if args.command=='reopen':
   if len(args.reason.strip())<12:parser.error('give a concrete reason (at least 12 characters)')
   start=list(STAGES).index(args.stage);receipts={n:v for n,v in receipts.items() if list(STAGES).index(n)<start};save(receipts)
   with (ROOT/'development/workflow-events.jsonl').open('a') as stream:stream.write(json.dumps({'event':'reopen','stage':args.stage,'reason':args.reason,'time':datetime.now(timezone.utc).isoformat()})+'\n')
   print(f'Reopened {args.stage} and all later stages; creative files preserved.');return
  if stale:parser.error(f'completed artifacts changed; reopen {stage} first')
  if args.stage!=stage:parser.error(f'complete stages in order; next stage is {stage or "none"}')
  if len(args.evidence.strip())<20:parser.error('provide a concrete evidence summary (at least 20 characters)')
  files,problems=artifacts(stage)
  if problems:parser.error('\n'.join(problems))
  receipts[stage]={'files':files,'evidence':args.evidence,'time':datetime.now(timezone.utc).isoformat()};save(receipts)
  print(f'Recorded {stage}. Run status for the next stage.')
 except (ValueError,OSError,KeyError) as error:parser.exit(1,f'{error}\n')


if __name__=='__main__':main()
