# Optional helper teams (advanced)

Most writers need only one conversation. Never lead onboarding with swarms, worker counts, agents, tokens, or configuration files. Say “I can check the research and continuity in parallel” only when useful. A helper team is an optional way to divide bounded research or review; it is not a requirement for producing a film.

Read development/teams.json if present. Missing configuration means off. Honor a writer's explicit current request and record any requested setting change. The default file is:

```json
{"mode":"off","max_workers":3,"max_rounds":1,"max_sources_per_worker":10,"allowed_tasks":["research","continuity","quality","package-review"],"allow_nested":false,"new_paid_services":false}
```

Modes: off means the coordinator does all passes sequentially; ask means propose the specific team and wait for consent before spawning; auto means native helpers may be used within recorded limits when the work benefits. A general writing request is not an instruction to enable a team. Validate settings before using helpers: mode must be off/ask/auto, worker cap 1–3, rounds 1–3, candidate sources per worker 1–20, task list a subset of the four listed values. Invalid or unsupported settings fall back to sequential work with an explanation, never larger defaults. Nested delegation and new paid services remain disabled; requests for a larger or external setup need a concrete separate decision.

## Check actual capability

Inspect tools exposed in this session and the host's current documentation when needed. An account name or paid subscription does not prove native subagents, concurrency, web access, remaining allowance, or context limits. Do not promise a feature before checking. Tell the writer only what affects their decision. If native workers are unavailable or allowance cannot support the plan, complete the work sequentially. Never buy a subscription, obtain API keys, launch a different model CLI, or upload a manuscript to a new service to simulate a team. Existing host usage can consume the writer's allowance; do not quote a spend ceiling as enforced when the host exposes no usage meter. Stop at a host usage limit and save a resumption point.

## Choose worthwhile assignments

Research: chronology, relationships, and context/challenge with disjoint source questions (see RESEARCH.md). Continuity: timeline, locations, physical objects and what characters know. Quality: a fresh full-draft diagnosis against the brief and rubric. Package review: compare selected materials to the actual script and identify unsupported claims. For a small excerpt or straightforward edit, a team adds little and sequential work is preferable.

Keep one coordinating author. Workers read a fixed draft fingerprint and write only their assigned notes directory, such as development/workers/continuity/. They never concurrently edit the screenplay, shared story bible, claims ledger, approvals or receipts. The coordinator integrates accepted changes and handles writer questions. Native workers running the same model are a second reading, not independent human or expert validation; disclose the actual setup.

Before spawning, write development/team_plan.json: selected mode, capability observed, draft fingerprint, objective, worker names/tasks/output paths, total worker cap (including nested), round/source limits, privacy restrictions, usage visibility, and stopping rule. Each assignment forbids further delegation. Give workers only necessary context; no need to duplicate private source material across tasks. Source/claim verification remains with the coordinator.

Afterward, write development/team_report.md with actual workers/rounds, files returned, disagreements, sources inspected, findings accepted/deferred, usage observed or unavailable, and unresolved limits. Multiple agreeing reports do not outvote contradictory evidence. If the screenplay changes, stale reviews must be repeated or explicitly scoped to the old draft. Do not fabricate workers, consensus or success. Team operation never authorizes outreach, purchases, publication or casting claims.
