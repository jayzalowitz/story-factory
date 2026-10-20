# Story development workflow

This is a story-specific adaptation of gstack's idea-to-delivery pattern: discovery, challenge, design, implementation, review, QA, and handoff. It runs with your coding agent; gstack itself is optional. The Python command tracks artifacts and stale work. It does not call models or decide whether art is good.

## Start or resume

Tell your agent:

> Read AGENTS.md, WORKFLOW.md, MASTER_PROMPT.md, and development/brief.md. Run `python3 scripts/workflow.py status`. Execute the next incomplete stage using WORKFLOW.md. Ask discovery questions when the seed is unclear; otherwise develop the artifacts, review them honestly, record evidence, and continue. Do not skip structural review to produce packaging early.

The stages apply to a complete feature package. For a smaller request, deliver the requested subset and report the remaining stages as unfinished. Never mark omitted work complete.

## 1. Discover: story office hours

Use a developmental conversation, not a questionnaire dumped on the writer. Ask the most consequential unanswered question first and follow the answer. Search the brief and existing material before asking something already answered. Offer a recommendation when alternatives would help. If the user asks you to make decisions, record your assumptions and proceed.

Explore these six questions:

1. What concrete person, situation, image, or contradiction made you want this story?
2. Who is this for, and what experience should they have that familiar stories are not giving them?
3. Who wants something badly enough to act, and what makes it difficult now?
4. What actual encounter, observation, research, or lived detail gives this idea specificity?
5. What is the smallest version that preserves the emotional force? What can we remove?
6. What change, question, or final image should stay with the audience afterward?

Challenge generic answers with a concrete example. Diagnose whether the seed has an engine or only a mood. Compare three distinct directions when the idea is loose. Recommend one, explain tradeoffs, and preserve the writer's explicit preferences. Never interpret an unanswered question as approval of a major creative commitment.

Save the filled brief and `development/discovery.md`: questions answered, distinguishing evidence, alternatives, chosen direction, assumptions, unresolved choices, and a short design brief. Record `Verdict: PASS` only when there is enough direction to develop a premise. Otherwise record `Verdict: REVISE` and the missing decision.

## 2. Challenge: premise and scope review

Act as a skeptical development executive, analogous to a CEO plan review. Is this the right movie? What is its strongest possible version? Identify the audience promise, dramatic engine, differentiation, central relationship, title promise, ending hypothesis, production envelope, and reasons someone would watch. Choose to expand, hold, or reduce scope with reasons.

Write `development/premise_review.md` and `development/story_bible.md`. Compare a contained execution and an ambitious execution; select based on the brief. Identify the three biggest creative risks and how scenes could test them. End the review with `Verdict: PASS` or `Verdict: REVISE`, evidence, and unresolved blockers. Do not award a pass merely because the premise sounds prestigious.

## 3. Design: character, form, and story architecture

Apply the equivalent of design and engineering plan reviews to dramatic experience and causality. Follow MASTER_PROMPT.md for characters, movement design, scene IDs, chronology, state changes, relationships, and production constraints.

Write `development/outline.md`, `development/scene_map.md`, `development/continuity.md`, and `development/structure_review.md`. Test protagonist agency, causal escalation, the middle, supporting-character choices, tonal range, formal rules, orientation, and the ending. Name specific weak sequences and repair them before writing 100 pages. The structure review records verdict, evidence, and remaining risks.

## 4. Draft: implement the movie

Write all screenplay files, using the architecture as a guide rather than filling slots mechanically. Keep continuity and scene IDs current. Use six source files initially; update the entry point if another organization serves the movie. Record the actual file inventory, completed sequences, unresolved research, and draft limitations in `development/draft_report.md`. A PASS means a complete readable draft exists, not that it is ready to send.

## 5. Review and revise: challenge the full draft

Read the entire screenplay from a fresh editorial posture. Follow the structural review questions in MASTER_PROMPT.md. Save `development/review.md`, prioritize consequential failures, implement revisions, and record specific interventions in `development/revision_log.md`. Update the story bible, outline, scene map, and continuity to reflect the revised movie. Re-read changed sequences in context.

The review must show findings, scene evidence, repairs, and remaining limitations. A PASS requires no unresolved issue that invalidates the central dramatic engine; smaller known weaknesses remain visible. Never manufacture universal agreement or claim independent review when only one agent reviewed the work. Model or human second opinions are optional unless the user requests them.

## 6. Package: derive the business and creative materials

Produce the development package and all 16 reader-specific pitches from the revised screenplay. Follow MASTER_PROMPT.md. Write `development/package_review.md` mapping claims to scene IDs, checking the ending and relationships, distinguishing proposed talent from attachments, and recording financial/research assumptions. Repair drift before passing.

## 7. Verify: story QA and publishing QA

Run `make all`. Check all 18 PDFs and all 16 one-page lengths. Render and inspect layout; record tools, commands, actual outputs, and visual observations. Search for scaffold placeholders and stale details. Perform a final continuity/readability review. Save `development/verification.md` with `Verdict: PASS` only when these checks actually pass. If a tool or check is unavailable, document the gap and leave this stage incomplete.

## 8. Handoff: delivery, not outreach

Update README and `development/status.md` with actual deliverables, measured page counts, known limitations, source links, and build instructions. Save `development/handoff.md` with the delivery inventory and a verdict. Share the local output or publish source only within the user's authorization. Repository publication does not authorize emailing pitches, contacting talent, or claiming attachments.

## Commands and evidence

```sh
python3 scripts/workflow.py status
python3 scripts/workflow.py check
python3 scripts/workflow.py complete discover --evidence "Brief and discovery reviewed; specific engine chosen."
python3 scripts/workflow.py reopen structure --reason "The ending changed, so causality needs another pass."
```

Complete stages in order. Every stage requires its output files, substantive content without scaffold markers, a PASS verdict in its review/report, and a written evidence summary. Each completion records hashes of its artifacts. Editing completed artifacts makes the workflow stale; `status` identifies the earliest affected stage. Reopen that stage explicitly and revalidate it and all later stages. Reopening preserves creative files and discards only completion receipts. Changing upstream material late in revision therefore requires rechecking upstream approvals; it does not require discarding the draft.

The mechanical gate catches missing, placeholder, and stale artifacts. The agent and writer remain responsible for truthful verdicts, creative judgment, facts, and visual verification. `complete verify` cannot by itself prove a build or visual review happened; its report must contain real evidence.
