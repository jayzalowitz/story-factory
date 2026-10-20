# Project instructions

Read CLAUDE.md, WORKFLOW.md, MASTER_PROMPT.md and development/brief.md. This is the toolkit source; create new stories in separate folders. Claude uses /story; Codex uses $story or /skills. Run scripts/workflow.py status in the actual story project. Use conditional true-story research, scene-evidenced quality/Bechdel reports, selected package outputs, real PDF evidence and honest handoff. Never claim mechanical checks establish creative quality. Optional teams follow TEAMS.md, off by default.

## Testing

```sh
python3 -m unittest discover -s story_factory -p 'test_*.py' -v
python3 -m unittest discover -s tests -v
node --check site/app.js
```

After changing command procedures, run python3 scripts/sync_skills.py. Mirror canonical story_factory workflow/check/package helpers into scripts and shared craft/workflow references into skills/story/references. Install/export behavior needs source-independent portability checks. Public site files are isolated under site/ and allowlisted by tests. Keep private research and generated installations out of Git.
