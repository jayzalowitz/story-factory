#!/usr/bin/env python3
"""Build an inspectable versioned source ZIP; excludes private and generated material."""
import argparse,hashlib,json
from pathlib import Path
import zipfile
ROOT=Path(__file__).resolve().parents[1]
FILES={'README.md','AGENTS.md','CLAUDE.md','CONTRIBUTING.md','MASTER_PROMPT.md','WORKFLOW.md','WRITING_GUIDE.md','Makefile','latexmkrc','.gitignore','install.py','COMMANDS.json','VERSION'}
DIRS={'story_factory','scripts','skills','common','fonts','screenplay','package','one_pagers','development','research','docs','examples','site','tests','.github'}
EXCLUDED={'.git','.context','.agents','.claude','__pycache__','private','output','delivery','dist','toolkit','node_modules','.venv','.DS_Store','Thumbs.db'}

def selected(root):
 for path in sorted(root.rglob('*')):
  relative=path.relative_to(root)
  if not path.is_file() or any(part in EXCLUDED for part in relative.parts) or path.is_symlink():continue
  if path.suffix in {'.pyc','.log','.aux','.out','.toc','.fls','.fdb_latexmk'}:continue
  if (len(relative.parts)==1 and relative.as_posix() in FILES) or (len(relative.parts)>1 and relative.parts[0] in DIRS):yield path

def build(root,destination):
 root=Path(root).resolve();destination=Path(destination).resolve()
 version=(root/'VERSION').read_text().strip()
 import re
 if not re.fullmatch(r'\d+\.\d+\.\d+(?:-[a-z0-9.]+)?',version):raise ValueError('Invalid release version')
 files=list(selected(root));manifest={'version':version,'files':{p.relative_to(root).as_posix():hashlib.sha256(p.read_bytes()).hexdigest() for p in files}}
 destination.mkdir(parents=True,exist_ok=True);target=destination/f'story-factory-{version}.zip'
 if target.exists():raise ValueError('Release archive already exists; preserve the reviewed artifact')
 prefix=f'story-factory-{version}/'
 with zipfile.ZipFile(target,'x',compression=zipfile.ZIP_DEFLATED) as archive:
  for path in files:archive.write(path,prefix+path.relative_to(root).as_posix())
  archive.writestr(prefix+'RELEASE_MANIFEST.json',json.dumps(manifest,indent=2)+'\n')
 (destination/(target.name+'.sha256')).write_text(hashlib.sha256(target.read_bytes()).hexdigest()+'  '+target.name+'\n')
 return target

if __name__=='__main__':
 parser=argparse.ArgumentParser(description=__doc__);parser.add_argument('--destination',type=Path,default=ROOT/'dist');args=parser.parse_args()
 print(build(ROOT,args.destination))
