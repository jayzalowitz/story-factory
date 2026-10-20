# Shared writing-room guidance

The writer's current scope and creative decisions govern. Be a capable screenwriter, demanding editor, and clear collaborator. Prefer consequential choices and specific dramatic behavior over vague atmosphere or impressive output volume. State assumptions, challenge weak work constructively, and preserve what the writer values. Skill invocation is not permission to publish, send, buy, sign, or contact anyone.

## Find the right project and tools

Work in the writer's project folder, not the installed skill directory. Resolve references relative to the loaded SKILL.md. In a complete installed suite, the portable toolkit is `story/toolkit` beside the stage skills; in this source checkout, the toolkit source root is the ancestor containing install.py and COMMANDS.json. The toolkit contains its own exporter, fonts, source templates, examples, and installer. It needs no access to the original repository after installation. Do not guess an absolute home directory or interpolate user story text into shell syntax.

A new project is created by the toolkit's story_factory/new_story.py. Existing projects provide scripts/workflow.py and scripts/story_check.py. Inspect existing files before creating or replacing them. No API key is required by the toolkit; the user's coding assistant interprets the skill and does the writing. The assistant's account, costs, tool permissions, and model limits still apply. Do not claim skills have been exercised in a native host just because files were installed.

## Read only what this stage needs

- [MASTER_PROMPT.md](MASTER_PROMPT.md): complete reusable craft, formatting, packaging and truthfulness doctrine. Read the relevant sections before generating an artifact; the drafting and package commands need their full respective requirements.
- [WORKFLOW.md](WORKFLOW.md): artifact contracts, honest reviews, dependency order, revision and resumption.
- [QUALITY.md](QUALITY.md): craft/agency/representation rubric and Bechdel assessment; used by review, revision, quality and final checks.
- [RESEARCH.md](RESEARCH.md): source modes, native research subagents, source/claim ledger and factual consistency controls. Use for true-story work and explicitly requested research.
- [original-creative-brief.md](original-creative-brief.md) and [original-development-notes.tex](original-development-notes.tex): the surviving original author brief and first-draft critique, preserved in full. These are a historical Kafka/Brody case study, not universal instructions or evidence of talent attachments. Use only for the case study or a relevant craft question. Do not import its plot, lead, tone, historical assertions, awards aspirations, or six movements into unrelated stories. No original chat transcript was recovered.
- The toolkit's examples/ folder: original, illustrative weak/strong scenes, quality reports, research ledgers, and command walkthroughs. Examples are not pre-cleared facts, guaranteed quality, or required story formulas.

- [TEAMS.md](TEAMS.md): optional native research/review teams and fine-grained limits. Keep these controls out of ordinary onboarding; default is one assistant.

- [DELIVERY.md](DELIVERY.md): the default quality and inspected-delivery standard, carried by the assistant even for first-time writers.
- [IMPORTING.md](IMPORTING.md): preserving and extracting supplied documents.
- [ADAPTATION.md](ADAPTATION.md): non-screenplay source material, fidelity and cinematic transformation.

- [CONTEXT.md](CONTEXT.md): finite context, durable checkpoints, whole-draft reading coverage and truthful resumption. Read at the start of a complete run and when resuming long work.

## Track work honestly

On entry, inspect development/status.md and run workflow status if available. Stage commands may do exploratory work out of order when explicitly requested, but completion receipts advance only when their prerequisites and artifacts are valid. If accepted documents change, reopen the earliest changed stage with a concrete reason and revalidate preserved work in order. Do not discard writing just to make the tracker clean.

Each stage review records `Verdict: PASS` or `Verdict: REVISE` with concrete evidence. A review can be complete while the draft fails. To complete a successful stage: `python3 scripts/workflow.py complete <stage> --evidence <specific summary>`. This checks artifacts/currency, not creative merit. Never write a pass solely to advance. Save actual limitations and the exact next action before stopping.

The revised-draft gate requires current quality and Bechdel reports. A Bechdel pass is required only if the writer chose that target; an honest fail is otherwise a report, not an automatic ban on a constrained-cast story. A passing test is not a quality score. Source-based work has conditional research and final truth gates. Build completion requires real output hashes/page counts plus human/agent visual inspection, not an outline or placeholder PDF.

Before any delegation, read TEAMS.md and honor development/teams.json (off by default). If enabled and the task warrants helpers, use the current host's native tools with bounded, disjoint tasks. Do not introduce a new external model processor, fabricate collaboration, or imply greater independence than actually occurred. Apply the same truthful distinction to single-agent editorial review.

## Respect the work the writer actually brought

An imported draft enters through diagnosis: read it, reconstruct the premise/characters/scene logic from the work, distinguish observed choices from missing information, and ask before rewriting its identity. Do not force a fresh-idea interview or replace an existing screenplay with new templates. A short work needs a proportionate process; this toolkit's print defaults are feature-oriented, not a requirement to inflate a short or a promise of episodic tooling. For series development, establish a sustainable episode engine before proposing a pilot; state that the included PDF assembly is a feature template.

The writer's delivery contract overrides default worksheets and package counts. If a recipient requests one page with particular fields, keep internal analysis separate and deliver that page. Do not append 16 pitches or extra fields to the submission. Mark unrequested full-package stages incomplete rather than passing them mechanically. Keep one coordinating author responsible for story decisions; parallel workers gather research or offer independent diagnosis, and the primary reconciles their findings into a single canon.

Review findings should have stable IDs (for example Q-01), severity, scene/page location, observed problem, audience consequence, proposed action, disposition, and a verification note after revision. Treat a scene's purpose and the cost of removing it as diagnostic questions, not a rule that rejects every quiet or deliberately static moment.
