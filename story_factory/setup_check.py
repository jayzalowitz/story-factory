#!/usr/bin/env python3
"""Read-only checks for the tools observed on this computer; never installs anything."""
import argparse
import json
from pathlib import Path
import platform
import shutil
import sys


def inspect_setup(project):
    root = Path(project).resolve()
    tools = {name: shutil.which(name) for name in ('claude', 'codex', 'python3', 'make', 'xelatex', 'latexmk', 'tectonic', 'pdfinfo', 'pdftotext')}
    hosts = {}
    for host, folder in [('claude', '.claude/skills'), ('codex', '.agents/skills')]:
        entry = root / folder / 'story/SKILL.md'
        hosts[host] = {'command_on_path': bool(tools[host]), 'project_skill_files_present': entry.is_file(), 'skill_entry': str(entry) if entry.is_file() else None, 'native_activation': 'not tested', 'account_and_usage': 'not checked'}
    issues = []
    if sys.version_info < (3, 9):
        issues.append('Use Python 3.9 or newer to run the project helpers.')
    if not any(h['project_skill_files_present'] for h in hosts.values()):
        issues.append('Project skills are not installed here. Ask your coding assistant to run the included installer for this project.')
    if not tools['pdftotext']:
        issues.append('PDF reading is unavailable: pdftotext is missing. Use a text, Fountain, Final Draft, or Word copy, or ask your assistant to help install Poppler.')
    missing_print = [name for name in ('make', 'pdfinfo') if not tools[name]]
    if tools['latexmk']:
        if not tools['xelatex']: missing_print.append('xelatex (the Makefile selects installed latexmk first)')
    elif not tools['tectonic']:
        missing_print.append('Tectonic or latexmk with XeLaTeX')
    if missing_print:
        issues.append('The included PDF build needs: ' + ', '.join(missing_print) + '. Writing and reviewing can continue before these are installed.')
    return {'schema_version': 1, 'project': str(root), 'python': {'version': platform.python_version(), 'supported': sys.version_info >= (3, 9)}, 'tools': tools, 'hosts': hosts, 'pdf_build_ready': not missing_print, 'issues': issues, 'limits': ['A program on PATH does not prove its login, subscription, remaining usage, or successful skill activation.', 'Desktop apps can work without command-line programs on PATH. Test the command inside your chosen assistant.', 'The Makefile selects latexmk first when installed; otherwise it can use Tectonic. Tool presence alone does not prove a successful build.', 'This check reads local state only. It does not install software, sign in, spend money, or contact a provider.']}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--project', default='.')
    parser.add_argument('--json', action='store_true', help='Print the observed checks as JSON')
    args = parser.parse_args()
    report = inspect_setup(args.project)
    if args.json:
        print(json.dumps(report, indent=2))
    else:
        print('Story Factory setup check\nProject: ' + report['project'])
        for host, state in report['hosts'].items():
            print(f"{host.title()}: project skill files {'found' if state['project_skill_files_present'] else 'not found'}; activation not yet tested.")
        print('PDF build tools: ' + ('found' if report['pdf_build_ready'] else 'some missing'))
        for issue in report['issues']:
            print('- ' + issue)
        print('\nNext: open this project in your assistant and invoke /story (Claude) or $story (Codex). Confirm it reads this project before proceeding.')
        print('Login, plan eligibility and usage limits must be checked in the provider’s own app. No account access was tested.')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
