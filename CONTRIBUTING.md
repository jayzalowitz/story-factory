# Contributing

Use a feature branch and a pull request for changes after the initial repository setup. Keep story-specific drafts in their own generated projects.

Canonical factory assets live in story_factory/. Keep root MASTER_PROMPT.md, WORKFLOW.md, and scripts/{workflow,story_check,package_options}.py synchronized with their factory counterparts. Do not commit ordinary build outputs, session context, credentials, or Python caches. Explicitly reviewed public example PDFs under site/examples/ and examples/the-night-window/pdfs/ are intentional exceptions. Preserve fonts/LICENSE.txt.

Run the tests and an independent export:

```sh
python3 -m unittest discover -s story_factory -p 'test_*.py' -v
python3 story_factory/new_story.py ../contribution-smoke --title "Contribution Smoke"
python3 ../contribution-smoke/scripts/workflow.py status
make -C ../contribution-smoke all
```

Check every expected PDF, all 16 pitch lengths, and changes to document layout. For prompt/playbook changes, also exercise the affected stage with a real example and distinguish mechanical test coverage from editorial evaluation.

For website changes, also run `python3 -m unittest discover -s tests -v` and follow the [website guide](docs/site/README.md). Publishable files must match the explicit public-artifact allowlist; do not copy private project material into site/.

The included CI runs Python workflow tests, public-site checks, and exporter smoke checks. It does not run model evaluations, compile PDFs, or judge story quality. Document those checks in the pull request when relevant.
