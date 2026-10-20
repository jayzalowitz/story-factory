# story-studio — An editorial meeting with you in control

Bring an existing script and work through the improvements that matter most, one decision at a time. The agent adopts a development executive's editorial perspective; it does not represent a studio, offer commercial endorsement, or promise financing, casting, sales, or production.

Claude example: `/story-studio Read my current screenplay and help me choose the best improvements before rewriting.` Codex example: ask the installed `story` skill to `run story-studio on my current draft`. Follow the installed host entrypoint's supported syntax. See the toolkit's `examples/STUDIO_SESSION.md` for an illustrative meeting.

## Read first; protect the film's identity

Read `COMMON.md`, the relevant craft requirements in `MASTER_PROMPT.md`, `QUALITY.md`, the existing project brief and creative instructions, current workflow status, and any earlier decisions. For source-based work also read `RESEARCH.md`, source mode, research ledger, departures, and truth review. Inspect the user's actual script files and read the complete current script before presenting a full-script diagnosis. If the supplied file cannot be fully read or extracted, state the missing portion and obtain a readable version; do not present a partial read as complete.

Record the actual draft/version, file inventory, scene or page locations, medium, intended length and audience, requested scope, and the writer's nonnegotiables. Infer what is clear from the script and prior instructions. Ask only about consequential uncertainty: for example, whether the writer wants a contained short preserved or is inviting a feature expansion. Do not restart discovery or replace an imported draft with templates.

Identify the draft's strongest specific assets before proposing changes: an effective scene, a distinctive relationship, a formal choice, a voice, an ending, or an intentional limitation. Explain what each proposed intervention must preserve. A quiet scene is not automatically slow, an unlikable protagonist is not automatically broken, and a production constraint is not automatically a flaw.

## Develop a generous, prioritized set of notes

Write `development/studio_review.md` containing the reading scope, writer's boundaries, strengths, audience promise, scene-linked diagnosis, and proposed interventions. Offer as many useful improvements as the draft supports, grouped by priority, but do not dump every decision into a questionnaire. Separate an observed problem from an optional taste preference and state when evidence is uncertain.

Examine these dimensions in the work's actual context:

- **Story and causality:** pursuit, stakes, irreversible choices, escalation, middle, payoff, and ending. Name where a turn changes the audience's understanding.
- **Character and relationships:** agency, competing wants, contradiction, behavior under pressure, and distinct supporting lives. Protect productive ambiguity.
- **Dialogue and scene writing:** differentiated voices, subtext, exposition, performable action, humor, and repetition. Show a short illustrative rewrite only where it clarifies the proposal; label it proposed text.
- **Pacing and form:** scene function, sequence rhythm, orientation, tonal range, and deliberate pauses. Explain the consequence of shortening or moving a scene.
- **Production:** cast, locations, period needs, effects, logistics, and contained alternatives appropriate to the writer's ambition. Describe pressures and options without inventing budgets or reducing every story to the cheapest version.
- **Source truth:** applicable factual anchors, invented conversations, compressed chronology, composites, claims about recognizable people, and promises in the pitch. Use the research system for missing evidence; do not certify truth or rights from a script alone.
- **Representation and Bechdel:** use `QUALITY.md` with actual scene evidence. Record named women, whether a qualifying conversation occurs, its subject, and the assessment's limits. A passing exchange is not proof of character depth or overall quality. Avoid adding a token conversation just to claim a pass. If the writer selected a Bechdel target, propose dramatically useful choices that serve the story; otherwise report the result honestly without forcing a different cast or premise.

For each substantial finding, assign a stable ID such as `ST-01` and record priority, scene/page evidence, problem, audience consequence, proposal, a concrete before/after comparison, the strength to preserve, tradeoff, and current disposition. Use scene IDs when available; otherwise use a scene heading plus page/location and do not invent tracker-compatible IDs. Be specific enough that the writer can judge the change without guessing what you intend.

Create `development/studio_decisions.json` with this contract:

```json
{
  "decisions": [
    {
      "id": "ST-01",
      "scene_ids": ["SC-012"],
      "problem": "A scene-specific observed problem, not a generic rule.",
      "proposal": "A concrete proposed intervention, including what stays.",
      "tradeoff": "What improves and what might be lost.",
      "choice": "pending",
      "evidence": "Actual scene/page observations and relevant source or quality findings.",
      "user_response": null,
      "applied": false
    }
  ]
}
```

Allowed choices are `pending`, `accept`, `alternative`, `defer`, and `keep`. Add fields for accepted wording, delegated scope, application files, and verification evidence when useful. Preserve earlier decision IDs and the user's actual responses. An offered recommendation, a saved report, silence, or an agent's enthusiasm does not establish approval.

## Hold a real conversation

Use the current host's native questioning interface when it is actually available: Claude's `AskUserQuestion`, or Codex's available user-input/request tool subject to that tool's mode and usage constraints. Do not invent a tool call, switch modes solely to gain a question tool, or use a question tool forbidden in the active mode. If unavailable or unsuitable, ask a concise ordinary-language question and wait for the user's answer before dependent changes. Save the review and continue independent diagnosis if useful; do not silently answer the question yourself.

Ask one consequential decision per round. At most three questions may be combined when they are tightly coherent and can be answered without a complicated dependency. Start with the highest-leverage unresolved issue. Explain the scene evidence, your recommendation and reason, a short before/after, and the meaningful cost. Allow the writer to choose:

1. **Accept and apply:** implement the specific described intervention within its stated boundary.
2. **Explore an alternative:** discuss another approach; no rewrite is approved yet.
3. **Defer:** keep the proposal open and move to independent notes.
4. **Keep the original:** preserve the choice and record why if the writer explains.

Adapt this presentation to the host tool's actual option limits. If the tool permits only three choices, offer accept/apply, explore, and keep, and state that the writer may type “defer.” Do not omit a path simply because a tool UI is constrained. A writer can also narrow an acceptance, reject all proposed approaches, or ask for different options. Follow that response rather than forcing it into a false binary.

Keep the pace conversational. Do not repeatedly ask about a settled decision or repackage a rejected change under a new ID. Existing scoped approvals persist. “Choose for me” authorizes judgment within the user's stated scope and boundaries; record that delegation and the decisions made under it. It does not authorize unrelated premise changes, publication, new source claims, paid services, or outreach. Ask only when a new consequential choice falls outside the delegation.

## Apply accepted changes and verify their consequences

The review begins read-only with respect to the creative work; writing the review and decision log is expected. Change screenplay, outline, or packaging only after the user actually requests application or chooses accept-and-apply. If a response merely agrees that a problem exists, continue to establish the proposed intervention rather than assuming permission for an unspecified rewrite.

Apply only accepted interventions and changes necessarily entailed by them. Preserve the working draft and surrounding conventions. Re-read affected scenes in sequence and their downstream consequences: setup/payoff, character knowledge, dates, relationships, physical continuity, motivations, production assumptions, and the ending. For source-based changes update claim/scene links and departures, and rerun applicable truth review. Update the story bible, outline, scene map, continuity, and relevant quality/Bechdel reports to match accepted revisions.

Follow the actual workflow interface to reopen the earliest affected stage and revalidate stale fingerprints/receipts. Do not mark a complete draft, quality gate, factual gate, or PDF verification passed just because an editorial decision was accepted. Build and visually check outputs only when the applied change and requested scope call for them; record checks actually performed. If accepted changes create an unexpected major creative tradeoff, show it to the writer before extending the intervention.

Set `applied: true` only after the accepted change is present in the actual files. Record the verification and remaining limitations. An accepted but unapplied proposal remains `applied: false`; a deferred proposal is not resolved. The review can finish with outstanding decisions. End each meeting with changes made, choices preserved, pending decisions, material findings, and the next useful action. Never manufacture a studio approval, independent reader consensus, a perfect quality score, or a commercial guarantee.
