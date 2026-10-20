#!/usr/bin/env python3
"""Render small host-neutral entrypoints from the command catalog and procedures."""
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
for item in json.loads((ROOT/'COMMANDS.json').read_text()):
    name=item['name'];folder=ROOT/'skills'/name
    folder.mkdir(parents=True,exist_ok=True)
    prefix='references' if name=='story' else '../story/references'
    text=f'''---
name: {name}
description: {json.dumps(item['description'])}
---

Read [{name} procedure]({prefix}/commands/{name}.md) and [shared operating guidance]({prefix}/COMMON.md), then carry out the user's request. Resolve these paths from this SKILL.md, not the project working directory. The complete craft guidance, research system, original case study, examples, and portable print toolkit live with the sibling `story` skill.

Use the input following the command as the writer's request. Claude Code invokes `/{name}`; Codex invokes `${name}` or its skill picker. Never run these chat commands in a shell. Do not turn a limited request into an unrequested full feature or claim a check that did not run.
'''
    (folder/'SKILL.md').write_text(text)
    (folder/'agents').mkdir(exist_ok=True)
    interface={'display_name':name.replace('-',' ').title(),'short_description':item['description'][:64], 'default_prompt':f'Use ${name} to help with my story project.'}
    (folder/'agents/openai.yaml').write_text('interface:\n'+''.join(f'  {key}: {json.dumps(value)}\n' for key,value in interface.items()))
print('Rendered skill entrypoints for Claude Code and Codex.')
