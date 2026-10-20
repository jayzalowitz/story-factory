# From a book, article, recording, or other source to a screenplay

A beginner can say, “Turn this material into a screenplay; help me make the choices.” The assistant owns the reading, craft analysis, revision, and delivery checks. Technical evidence stays in the project; explain choices in ordinary language. Adaptation is a creative relationship to source material, separate from `original`, `based-on`, or `inspired-by`, which describe a truth promise. A fictional novel adaptation can be `original` for factual research purposes. A memoir can need both adaptation and true-story reviews.

## Read before deciding

Preserve supplied files without overwriting them. Inventory each edition, transcript, recording, or article in `adaptation/project.json`, version 1. Record ID, title, kind, project-relative path, SHA-256, provenance, locator scheme, integer units and read_units. Units can be chapters, pages, numbered paragraphs, or transcript segments; define the unit precisely. Read the entire agreed adaptation source, not just its synopsis. If only an excerpt is supplied, describe the scope as that excerpt and request missing material before claiming the whole work is covered. Record OCR gaps, missing pages, ambiguous speakers, inaccessible audio and transcription uncertainty. A checked hash proves which file was considered, not that an assistant read it.

Kinds: novel, memoir, article, play, oral-history, podcast, short-story, nonfiction, other. Source-use status: user-owned, permission-recorded, public-domain-asserted, unresolved. Each status needs a specific basis, including territory/edition/translation limits when relevant. Ask what permission the writer actually has; do not declare legal clearance or confuse permission to read with permission to adapt. Do not fetch unauthorized full texts or reproduce copyrighted passages at length. A public URL is not a rights grant. Unresolved source-use questions permit private analysis and original alternatives but block a delivery labeled ready for external use.

## Make a small number of meaningful choices

Explain the proposed movie in a paragraph. Agree the length, intended audience, viewpoint, dramatic question, ending, and fidelity promise. Store contract.scope, contract.preserve, contract.change_policy, and status proposed/approved. Use the host's supported question interface for consequential choices; provide options, recommendation and concrete effects. Approve classes of small cinematic changes once instead of repeatedly asking about punctuation. If no question interface is available, ask a numbered plain-language question and wait for the needed answer. Do not silently interpret “faithful” as “everything survives.”

Map source units into dramatic beats. Identify the active protagonist, opposing force, choices, reversals and ending. Convert interior thought into observable behavior, sound, conflict and consequence. Evaluate voice-over for a specific dramatic function. Compress repetition and chronology without reversing cause and effect. Select the film's story rather than illustrating every chapter. Preserve supporting characters' agency; do not add a token conversation solely to manufacture a quality-test pass. Match the requested tone; dry wit is a craft choice, not a universal instruction.

Track approved changes in departures: stable id, description, reason, decision proposed/approved/rejected/deferred. Include omitted events, merged characters, changed viewpoint/chronology, new ending and invented dialogue. Honor rejections. Major unapproved departures block readiness. Inherited source limitations should be explained to the writer rather than covered by a disclaimer.

## Write, inspect, repair

Use a stable `% scene: S001` marker in TeX, `# scene: S001` in Markdown or `// scene: S001` in Fountain. Every screenplay scene gets a corresponding scenes entry: id, source_refs [{source_id, locator}], transformation, departure_ids, and invention_reason for wholly invented scenes. A source reference is not a claim that dialogue is quoted. Link factual scenes to research claim IDs as well when applicable.

Write the complete requested screenplay. Then perform a full-draft editorial read and targeted substantive repairs: causality, character decisions, cinematic writing, pacing, dialogue, continuity, source fidelity, truth promise and selected package consistency. Beginners receive this work automatically; do not lower the standard because they cannot diagnose weaknesses. Never award READY merely for completing files or producing a long draft.

Run `python3 scripts/adaptation.py check` while developing. After actually reviewing the complete current draft, write adaptation/review.md with findings, repairs, unresolved issues and scope. Write review.json with coverage full-draft, draft_sha256 from the helper, record_sha256 of project.json, source_sha256 mapping each source ID to its current file hash, verdict READY/REVISE and a substantive summary. Run `python3 scripts/adaptation.py current`. This checks evidence consistency and currency, not literary merit or legal safety. A changed source, screenplay, map or fidelity decision requires rereading affected material and renewing the review. Run the separate craft, Bechdel, factual and PDF checks that apply. Keep the same polished delivery bar as original screenplays.

## Record shape

See `examples/adaptation/adaptation/project.json` and its reviewed short. Those approvals are demonstration assumptions made by the authoring agent, not a historical user interview. Never copy their decisions into a writer's project. Keep the example's source-use assertions separate from legal certification.
