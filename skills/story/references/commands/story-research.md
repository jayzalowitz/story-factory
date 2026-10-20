# story-research — Find the truth your story needs

Use this when a story draws on real events or when an invented world needs credible detail. In Claude Code, invoke `/story-research`; in Codex, invoke `$story-research` or use the skill picker. Follow the host entrypoint's supported syntax; this file does not install a command by itself.

Examples:

> /story-research My invented thriller follows a night-shift ferry dispatcher. Research the work and constraints, keeping the characters fictional.

> /story-research This is based on my grandmother's account of a factory closure. Build the chronology, check what public records support, and keep the family's private letters private.

> /story-research Inspired by a real rescue, but a different place and invented characters. Help define what we are borrowing and what we are creating.

Read `COMMON.md`, `TEAMS.md`, `RESEARCH.md`, the user's brief and supplied material, the relevant original guidance, and existing workflow status. Do not research a real subject merely because these examples exist.

1. Establish `original`, `based-on`, or `inspired-by` and record `research/source_mode.json`. Preserve the user's intended truth promise and creative restrictions. If a consequential choice is unknown, ask a short question; otherwise state assumptions and proceed.
2. Write `research/plan.md` with subject, period, purpose, exclusions, questions, bounded source/worker budget, and assignment manifest. Defaults: coordinating parent plus up to three native workers; ten candidate sources per worker; one pass. Fewer workers are appropriate for a small question.
3. Honor development/teams.json: off means sequential passes; ask requires consent; auto permits bounded helpers. Use the current approved host's actual native subagents when enabled and available, with the disjoint chronology, relationships, and context directories in `RESEARCH.md`. No new model service, external CLI processor, or recursive worker tree. If unavailable, explicitly report the sequential fallback and complete the same passes yourself. Read-only web research is within this command's scope; contacting sources, buying access, uploading private material to a new service, and publication require separate authorization.
4. Gather source-first notes, exact locations, access dates, candidate claims, contrary evidence, and research limits. Prefer records closest to the event while checking provenance and perspective. Never cite a source you have not inspected as if you had.
5. Reconcile reports in the parent. Inspect decisive evidence, distinguish independent corroboration from repeated retellings, resolve only what evidence permits, and build `research/claims.json`.
6. Produce `chronology.md`, `relationships.md`, `context.md`, `open_questions.md`, and `source_material.md` under `research/`. Connect each factual assertion to claim IDs and each finding to a dramatic implication. Record explicit departures and relevant living-person concerns without claiming legal clearance.
7. Update `research/scene_traceability.md` for existing scenes, or record that scenes are not yet drafted. Recommend concrete premise/outline changes. Run `story-truth` when the real-story gate is applicable; do not mark research as a completed factual review by itself.

Finish with the selected mode, the best-supported discoveries, unresolved contradictions, files actually created, actual delegation or sequential execution, and what this changes for the story. Distinguish completed research from planned research. If tools or key sources are unavailable, report that limit and keep claims unverified.

Write research/report.md with actual findings, inspected decisive sources, disagreements, completed delegation (or fallback), limits and `Verdict: PASS` or `Verdict: REVISE`. For source-based modes, the research stage requires plan.md, report.md, claims.json, and truth_report.md. Use story-truth for a concept/outline audit before completing research; after a draft exists, repeat the truth audit against the actual screenplay.
