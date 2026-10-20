# How this project was made, and how to reuse it

This repository preserves a creative operating brief, a modular publishing system, and an unusually detailed revision history. It does not contain a standalone story-generation API or the original conversation transcript. The reconstruction below is based on tracked source and commits; the exact instructions or automation behind the “studio loop” were not recovered.

## What the history establishes

| Stage | Evidence | What it tells us |
|---|---|---|
| Creative instructions first | `21a8e9e`, March 31, 2026; `CLAUDE.md` | A detailed project doctrine specified the concept, lead-actor target, psychology, themes, mandatory scenes, quality rules, source structure, and expected deliverables. |
| Full first build | `dd37f24`, March 31 | Six screenplay movements, studio package, early pitches, LaTeX macros, and Makefile arrived together. The commit credits Claude Opus 4.6 as co-author; that is evidence of an AI-assisted build, not a complete account of every tool used. |
| Development review | `dd37f24:package/script_notes.tex` | The first tracked build included a frank review: the screenplay had identity and atmosphere but needed propulsion, protagonist agency, distinct relationships, a recurring office case, tonal variation, and title payoff. |
| Structural response | `0323313`, March 31 | Revisions introduced a recurring sawmill case, a promotion refusal, stronger supporting-character decisions, chronology repairs, and updated package materials. Script notes were removed from the outward-facing package; the commit says they were archived under `.context/`. They remain retrievable from Git. |
| Iterative studio pass | 116 commits labeled `studio loop: cycle 001` through `116` | The revisions covered story pressure, pitches for more audiences, dialogue, stageable action, cross-document alignment, typography, font portability, and compilation warnings. Commit labels alone do not establish the loop's scheduler, model, or exact prompt. |
| Another substantive rewrite | `f5d5fdd`, April 1 | Even after those cycles, a new structural assessment led to harder protagonist choices, the father's return, conflict for Dora, stronger voices, and escalating formal devices. |
| Redistribution and finishing | `8c4386b`, `42e834f`, `c6f1093`, `1b645b7`, `b91ffbf` | Material moved between acts, package descriptions caught up, an independent Julie–Ottla scene was added, and final metadata/formatting repairs followed. |

The repeatable method is **creative doctrine → complete draft → candid structural diagnosis → consequential revision → prose and performance passes → synchronized packaging → PDF verification**. The 116 cycles are a historical observation, not a recommended quota.

## The most useful original files

- `CLAUDE.md`: the original long creative directive; the closest surviving artifact to a master prompt. It is highly specific to Kafka and Adrien Brody.
- `common/screenplay_macros.tex`: reusable scene, action, cue, dialogue, parenthetical, transition, and title-card commands.
- `common/studio_package_macros.tex`: reusable sections, scene cards, targets, comparable-film entries, and risks.
- `common/typography.tex`, `common/colors.tex`, and `fonts/`: portable typography and package appearance. Keep the font license with the fonts.
- `common/metadata.tex`: the intended shared project identity, although some originals also hardcode title/casting language elsewhere.
- `screenplay/main_screenplay.tex` and `package/studio_package.tex`: modular document assembly.
- `Makefile` and `latexmkrc`: compilation of 18 PDFs, using Tectonic or latexmk/XeLaTeX. This compiles writing; it does not generate stories.
- `screenplay/`, `package/`, `one_pagers/`: worked examples for structure and audience-specific copy. Their content is project-specific and should be replaced for a new story.

The final README describes a 106-page screenplay and a 45-page package. Those are recorded claims from the existing project, not newly measured page counts in this investigation. The core package has 15 included content modules plus its assembly file. There are 16 pitch documents total.

## Use the new master prompt

[MASTER_PROMPT.md](../MASTER_PROMPT.md) is a self-contained, genre-flexible prompt covering the brief, story bible, character design, scene map, screenplay, structural review, revision loops, full development package, 16 pitches, research discipline, compilation, and handoff.

[WORKFLOW.md](../WORKFLOW.md) adds a gstack-inspired execution system: story office hours, premise and scope review, character/structure design, drafting, editorial revision, packaging, QA, and handoff. Exported projects include `scripts/workflow.py` to track required artifacts, review verdicts, evidence, and stale completion receipts. It works with your coding agent and does not require gstack to be installed.

Paste it into a coding agent with filesystem access, or give the agent the file path. Fill in its project brief first. It can also guide a chat-only writing session, but file creation and PDF verification require suitable tools. The prompt is newly written guidance, not a verbatim recovered prompt.

## Create a blank project with the existing code

From this repository root, run:

```sh
python3 story_factory/new_story.py ../my-new-film --title "My New Film"
```

The destination must not exist. The exporter copies the working layout, build rules, local fonts and licenses, and document entry points. It creates blank six-part screenplay files, 15 package modules, 16 pitch documents, neutral metadata, a brief, status notes, agent instructions, and the master prompt. It removes the original story and neutralizes the shared style's Kafka-specific identifiers. It does not initialize Git or install dependencies.

Then open the new directory, complete `development/brief.md`, and tell your agent:

> Read MASTER_PROMPT.md and development/brief.md. Execute the requested scope, beginning with the development plan. Replace the scaffold placeholders with complete original writing and verify the resulting documents.

Build once tools are installed:

```sh
cd ../my-new-film
make all
```

The blank project is intentionally compilable. Its PDFs remain labeled as placeholders. A successful blank build proves only that the publishing system works. The exporter does not call an AI model; the coding agent follows the prompt to create the story. Six files are a starting organization, not a requirement for six acts or title pages.

The starter script must run from this source repository, because it exports the source assets. Once generated, the new project builds independently and needs no access to this repository. No bundled `.claude/skills`, Git history, private `.context` material, original prose, or actor-specific claims are exported.

Validation in this workspace: a generated scaffold compiled all 18 PDFs with Tectonic; all 16 pitches measured exactly one page. Extracted text confirmed placeholder labeling, and PDF metadata preserved a title containing ampersand, percent, and underscore characters. The build log contained no overfull/underfull diagnostics or errors. The exporter also passed checks for neutral source, expected files, and refusing an existing destination. These are build and content checks, not visual approval of a finished screenplay or package.

## Inspect the development evidence yourself

Run these commands in the [original repository](https://github.com/jayzalowitz/the-letter-to-the-father), not the standalone Story Factory repository. References above to original source files also describe that original repository.

```sh
git show 21a8e9e:CLAUDE.md
git show dd37f24:package/script_notes.tex
git show 0323313 -- screenplay package
git log --reverse --oneline --grep='studio loop:'
git show f5d5fdd -- screenplay
```

The important improvement in the new prompt is ordering: test dramatic causality before investing in hundreds of small prose changes, then derive every pitch from the screenplay that actually exists. It also makes casting status, research uncertainty, budget assumptions, and final verification explicit.
