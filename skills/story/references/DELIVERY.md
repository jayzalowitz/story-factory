# The assistant carries the quality standard

A beginner supplies taste, creative boundaries and decisions, not specialist prompts. The default run includes the same craft and production checks as an expert-led run. Teams and memory are optional accelerators, never prerequisites for quality. Do not produce a shorter or weaker deliverable because the writer lacks technical vocabulary.

Before drafting: choose a specific dramatic engine, characters with competing wants, causal outline and ending; establish tone and constraints. For adaptation, fully read the selected source scope and establish fidelity; for factual material, inspect sources and distinguish facts from invented scenes. Ask important creative choices one at a time.

Before packaging: read the whole draft once, diagnose actual scenes, repair consequential flaws, and re-read changed sequences with their setups/payoffs and downstream continuity. Preserve strengths. Dialogue must be performable and differentiated; interiority must be made cinematic. Check agency, emotional range, deliberate humor/dry restraint when appropriate, supporting lives, ending and title payoff. A Bechdel exchange is evidence, not a substitute for dimensional people.

Use one author, one initial full-draft diagnosis, and targeted repair/review passes. Add a fresh full read after structural changes or when local fixes cannot establish coherence. Do not re-send the whole project through every model. Set a bounded review plan; after two repair rounds, show any consequential unresolved issue and save an exact continuation point rather than cycling to manufacture READY. Use available smaller models only for tasks they can verify reliably; preserve strong story judgment for consequential choices. Account usage that is not exposed is unknown, never zero. No new paid processor or automatic upgrade.

The original feature and The Night Window show the desired class of complete, coherent, restrained, readable output. They are references, not story templates or a guarantee of equivalent artistic success. Measure against concrete scenes and reader experience, not file count or a numeric score.

Build only selected materials with story_check.py build. Render and inspect EVERY page of delivered PDFs, including covers, scene transitions, dialogue continuations and each pitch. Fix clipping, isolated cues, accidental blank/divider pages, excessive whitespace and overflow without shrinking text below readable sizes. Check package claims against the actual revised screenplay. Do not invent attachments, financing, awards, rights clearance or professional endorsement.

Record actual inspection in development/visual_review.json:

```json
{"outputs":{"screenplay.pdf":{"sha256":"ACTUAL_HASH_FROM_BUILD","pages_inspected":[1,2,3],"verdict":"PASS","observations":"Actual page-by-page layout findings and repairs."}}}
```

Each selected PDF needs its actual hash and every physical page number in order. Never fill this before rendering/inspection. The helper checks currency and coverage declarations, not whether a person or agent actually looked. For large documents use contact sheets plus full-resolution checks where text/boundaries are uncertain; disclose inspection limits.

Write handoff.md with honest unresolved limits, then run python3 scripts/delivery.py. It checks current draft, build, factual/adaptation and all-page visual receipts, creates a new local folder with only selected PDFs and editable print inputs, and records a manifest. It never sends anything. Unselected PDFs, private originals, credentials and runtime sessions stay outside the delivery. If blocked, explain the specific repair, keep writing safe, and do not call the project complete.

When the writer sets a hard screenplay length cap, record screenplay_max_pages in development/preferences.json as the total physical PDF page limit, explicitly allowing for the chosen cover/title material. The checker rejects an over-limit build/receipt. Do not reinterpret “two dramatic pages” as three, add an isolated end page, or silently waive the requested scope. Drafting/revision must fit the actual brief; count compliance alone still does not establish quality. Do not repeat a successful build without changed sources or a specific unresolved concern.
