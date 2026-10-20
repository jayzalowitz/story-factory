# Contributing

Use a feature branch and a pull request for changes after the initial repository setup. Keep story-specific drafts in their own generated projects.

Canonical factory assets live in story_factory/. Keep root MASTER_PROMPT.md, WORKFLOW.md, and scripts/workflow.py synchronized with their factory counterparts. Do not commit generated PDFs, session context, credentials, or Python caches. Preserve fonts/LICENSE.txt.

Run the tests and an independent export:

```sh
python3 -m unittest discover -s story_factory -p 'test_*.py' -v
python3 story_factory/new_story.py ../contribution-smoke --title "Contribution Smoke"
python3 ../contribution-smoke/scripts/workflow.py status
make -C ../contribution-smoke all
```

Check every expected PDF, all 16 pitch lengths, and changes to document layout. For prompt/playbook changes, also exercise the affected stage with a real example and distinguish mechanical test coverage from editorial evaluation.

The included CI runs Python workflow tests and exporter smoke checks. It does not run model evaluations, compile PDFs, or judge story quality. Document those checks in the pull request when relevant.
