#!/usr/bin/env python3
"""Install the same portable Story Factory skills for Claude Code and Codex."""
import argparse
import hashlib
import json
from pathlib import Path
import shutil
import tempfile

ROOT = Path(__file__).resolve().parent
MARKER = '.story-factory-owned.json'
IGNORE = shutil.ignore_patterns('__pycache__', '*.pyc', 'toolkit', '.git', '.claude', '.agents', 'output', '.context', 'private', 'delivery', 'dist', MARKER)
PAYLOAD_FILES = ['Makefile', 'latexmkrc', '.gitignore', 'install.py', 'COMMANDS.json', 'MASTER_PROMPT.md', 'WORKFLOW.md', 'WRITING_GUIDE.md']
PAYLOAD_DIRS = ['story_factory', 'common', 'fonts', 'screenplay', 'package', 'one_pagers', 'skills', 'examples']


def hashes(directory):
    return {p.relative_to(directory).as_posix(): hashlib.sha256(p.read_bytes()).hexdigest()
            for p in directory.rglob('*') if p.is_file() and p.name != MARKER and '__pycache__' not in p.parts and p.suffix != '.pyc'}


def install(project, host='both', check=False):
    catalog = json.loads((ROOT / 'COMMANDS.json').read_text())
    hosts = ['claude', 'codex'] if host == 'both' else [host]
    targets = []
    # Preflight every destination before changing any host or skill.
    for name in hosts:
        base = project / ('.claude' if name == 'claude' else '.agents') / 'skills'
        if base.is_symlink() or any(p.is_symlink() for p in [base.parent, project]):
            raise ValueError(f'Refusing a symlinked installation target: {base}')
        for entry in catalog:
            target = base / entry['name']
            if target.is_symlink():
                raise ValueError(f'Refusing a symlinked skill: {target}')
            if target.exists():
                receipt = target / MARKER
                if not receipt.is_file():
                    raise ValueError(f'Existing skill is not owned by Story Factory: {target}')
                old = json.loads(receipt.read_text())
                if old.get('owner') != 'story-factory' or hashes(target) != old.get('files'):
                    raise ValueError(f'Installed skill has local changes; preserve them before reinstalling: {target}')
            elif check:
                raise ValueError(f'Skill not installed: {target}')
            targets.append((entry, target))
    if check:
        print(f'Checked {len(targets)} installed skills; ownership and content intact.')
        return
    with tempfile.TemporaryDirectory(prefix='story-factory-install-') as temp:
        prepared = Path(temp)
        for entry in catalog:
            name = entry['name']
            shutil.copytree(ROOT / 'skills' / name, prepared / name, ignore=IGNORE)
        toolkit = prepared / 'story' / 'toolkit'
        toolkit.mkdir()
        for name in PAYLOAD_FILES:
            shutil.copyfile(ROOT / name, toolkit / name)
        if (ROOT / 'VERSION').is_file():
            shutil.copyfile(ROOT / 'VERSION', toolkit / 'VERSION')
        for name in PAYLOAD_DIRS:
            shutil.copytree(ROOT / name, toolkit / name, ignore=IGNORE)
        for entry in catalog:
            folder = prepared / entry['name']
            (folder / MARKER).write_text(json.dumps({'owner':'story-factory', 'schema':1, 'files':hashes(folder)}, indent=2)+'\n')
        for entry, target in targets:
            target.parent.mkdir(parents=True, exist_ok=True)
            if target.exists():
                # Only verified installer-owned, unmodified content reaches this replacement.
                shutil.rmtree(target)
            shutil.copytree(prepared / entry['name'], target)
    print(f'Installed {len(catalog)} skills for {", ".join(hosts)} in {project}.')
    print('Claude Code: /story   |   Codex: $story (or /skills). Reopen the session if needed.')


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    where=parser.add_mutually_exclusive_group()
    where.add_argument('--project', type=Path, default=None, help='Project folder; defaults to the current directory')
    where.add_argument('--user', action='store_true', help='Explicitly install under your home directory for all projects')
    parser.add_argument('--host', choices=['both','claude','codex'], default='both')
    parser.add_argument('--check', action='store_true', help='Inspect an existing installation without writing')
    args=parser.parse_args()
    project = Path.home() if args.user else (args.project or Path.cwd()).expanduser().absolute()
    try:
        install(project, args.host, args.check)
    except (ValueError, OSError, KeyError, json.JSONDecodeError) as error:
        parser.exit(1, f'Story Factory: {error}\n')


if __name__ == '__main__':
    main()
