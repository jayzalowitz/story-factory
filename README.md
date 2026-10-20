# Story Factory

Turn a story idea into a complete feature screenplay, development package, and 16 stakeholder pitches through a staged, evidence-backed workflow.

Inspired by gstack's product-development pattern: office hours → premise/scope review → character and structure design → draft → critical review and revision → package → QA → handoff. This is a story-specific adaptation, not an official gstack component. It works with a coding agent; gstack is optional.

## Start a new story

Clone this repository, then create a fresh project:

```sh
git clone https://github.com/jayzalowitz/story-factory.git
cd story-factory
python3 story_factory/new_story.py ../my-film --title "My Film"
cd ../my-film
```

Python 3.9+ is required. The destination must not exist. The generated project is independent of this repository. The exporter preserves layout, fonts, and publishing rules; it exports no existing screenplay, agent sessions, or original Git history.

Give your coding agent this instruction:

> Read AGENTS.md, WORKFLOW.md, MASTER_PROMPT.md, and development/brief.md. Help me discover the story from my idea. Run `python3 scripts/workflow.py status`, execute the next stage, challenge weak assumptions, write the real artifacts, and continue through revision and verification. Ask the most consequential unanswered question first. Preserve my explicit creative choices.

Supply your seed idea in the conversation or development/brief.md. The agent uses the [master prompt](MASTER_PROMPT.md) for craft requirements and the [workflow](WORKFLOW.md) for execution. Do not use this template repository itself as your first story unless you intentionally want to maintain your story and template together.

## The development system

| Stage | Purpose | Main evidence |
|---|---|---|
| Discover | Story office hours: specificity, audience experience, engine, constraints | Brief and discovery design document |
| Premise | Challenge the idea, compare scopes, choose a direction | Story bible and premise review |
| Structure | Design characters, causality, movement, chronology, and form | Outline, scene map, continuity, structure review |
| Draft | Write the complete screenplay | Actual screenplay files and draft report |
| Revise | Find structural failures, implement repairs, then polish | Review and revision log |
| Package | Derive consistent development and stakeholder materials | Studio package, 16 pitches, package review |
| Verify | Check story continuity and compile/inspect the documents | Verification report with real evidence |
| Handoff | Deliver editable source and measured outputs | README, status, handoff inventory |

The workflow command enforces stage order, required artifacts, no placeholder content, explicit review verdicts, and written completion evidence. Receipts hash reviewed files; upstream edits invalidate completion until revalidated. It does not call an AI service or certify creative quality. The agent and writer must supply honest editorial judgment and actual verification evidence.

```sh
python3 scripts/workflow.py status
python3 scripts/workflow.py check
python3 scripts/workflow.py complete discover --evidence "Reviewed the concrete story engine and direction."
python3 scripts/workflow.py reopen structure --reason "The ending changed and causality needs another review."
```

## Build PDFs

Install Tectonic, or latexmk with XeLaTeX. For example, on macOS with Homebrew:

```sh
brew install tectonic
make all
```

Individual targets: `make screenplay`, `make package`, `make one-pagers`. Outputs go in output/: screenplay.pdf, studio-package.pdf, and 16 pitch PDFs. Tectonic may download its TeX support files on the first build. Local fonts and their license are included.

The blank project compiles intentionally. Its documents are labeled as placeholders, and workflow completion remains blocked until actual writing exists. Mechanical build success is not story approval.

## Repository map

- MASTER_PROMPT.md: detailed reusable writing and packaging requirements.
- WORKFLOW.md: stage-by-stage agent playbook, review criteria, and handoff rules.
- story_factory/: exporter and its self-contained workflow sources.
- scripts/workflow.py: workflow command for this template project.
- common/, fonts/, Makefile, latexmkrc: reusable publishing infrastructure.
- screenplay/, package/, one_pagers/: blank content templates.
- development/: brief, progress, and review evidence.
- docs/ORIGIN.md: reconstruction of the original project's development history.

The root copies of MASTER_PROMPT.md, WORKFLOW.md, and scripts/workflow.py mirror their canonical versions in story_factory/. When changing the factory, update the root copies too. The original prototype was developed in the-letter-to-the-father; no original screenplay prose is included here.

## Developer checks

```sh
python3 -m unittest discover -s story_factory -p 'test_*.py' -v
python3 story_factory/new_story.py ../export-smoke --title "Export Smoke"
make -C ../export-smoke all
```

Checks cover sequencing, missing evidence, review/placeholder failures, stale artifacts, and safe reopening. Export smoke checks should also confirm all 18 PDFs exist and all 16 pitches are one page. No external API key is needed; creative execution uses whichever coding agent you provide. Publishing this repository does not authorize outreach or imply talent attachments.
