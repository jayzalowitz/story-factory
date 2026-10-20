#!/usr/bin/env python3
"""Safely refresh project helper scripts; never edits manuscripts or writer decisions."""
import argparse,hashlib,json
from pathlib import Path
import shutil
HELPERS=['workflow.py','story_check.py','package_options.py','setup_check.py','import_source.py','adaptation.py','team_controls.py','delivery.py','upgrade_project.py']

def sha(path):return hashlib.sha256(path.read_bytes()).hexdigest()

def plan(project,source):
 project=Path(project).resolve();source=Path(source).resolve();folder=project/'scripts'
 if not project.is_dir():raise ValueError('Choose an existing story folder')
 if folder.is_symlink():raise ValueError('Refusing symlinked scripts folder')
 marker=project/'.story-factory-tools.json'
 if marker.is_symlink():raise ValueError('Refusing symlinked ownership record')
 record=json.loads(marker.read_text()) if marker.is_file() else {'files':{}}
 if not isinstance(record,dict) or not isinstance(record.get('files'),dict):raise ValueError('The helper ownership record is invalid; preserve it for review')
 owned=record['files']
 previous=[]
 for host in ['.claude','.agents']:
  old=project/host/'skills/story/toolkit/story_factory'
  if old.is_dir() and old.resolve().is_relative_to(project):previous.append(old)
 result=[]
 for name in HELPERS:
  incoming=source/name;target=folder/name
  if not incoming.is_file():raise ValueError('Release is missing helper: '+name)
  if target.is_symlink():raise ValueError('Refusing symlinked helper: '+name)
  if target.exists():
   current=sha(target)
   if current!=owned.get('scripts/'+name) and not any((old/name).is_file() and sha(old/name)==current for old in previous):
    raise ValueError('Preserve locally modified or unowned helper before upgrading: scripts/'+name)
  result.append((incoming,target))
 return result

def upgrade(project,source):
 project=Path(project).resolve();items=plan(project,source)
 for incoming,target in items:
  target.parent.mkdir(parents=True,exist_ok=True);shutil.copyfile(incoming,target)
 (project/'.story-factory-tools.json').write_text(json.dumps({'schema':1,'files':{'scripts/'+target.name:sha(target) for _,target in items}},indent=2)+'\n')
 return len(items)

if __name__=='__main__':
 parser=argparse.ArgumentParser(description=__doc__);parser.add_argument('--project',required=True,type=Path);parser.add_argument('--check',action='store_true');args=parser.parse_args()
 try:
  source=Path(__file__).resolve().parent
  if args.check:print('Helper upgrade preflight passed:',len(plan(args.project,source)))
  else:print('Refreshed helpers:',upgrade(args.project,source))
 except (ValueError,OSError) as exc:parser.exit(1,str(exc)+'\n')
