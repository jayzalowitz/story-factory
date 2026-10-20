# An illustrative studio meeting

This is a newly invented example of how `story-studio` can work. It is **not a transcript**, an actual user approval, a reviewed screenplay, a researched true story, or a claim that tools or file edits ran. The screenplay and decisions below are fictional. In a real session the agent reads the complete supplied script and records only actual responses and edits.

## The writer's request

> Read *Last Frequency*, my 24-page short about a radio operator during a storm. I want substantial notes, but keep the two-location production plan, the sibling relationship, and the unresolved ending. Ask me before rewriting.

The agent reads the entire draft, its brief, and previous decisions. It records that the story is original fiction. The absence of a real event means the fictional plot does not need a true-story certification; any later factual claims about radio practice would still need appropriate checking.

## The review comes before the questions

The agent saves a prioritized review. Its strongest observation is that the sibling argument on pages 8–10 creates tension through interrupted work rather than explanatory speeches. Any revision should preserve that behavior. The production limit is a deliberate strength: the audience hears danger through calls and must imagine it.

| ID | Priority and evidence | Proposed improvement | Before / after and tradeoff |
| --- | --- | --- | --- |
| ST-01 | High: in SC-012, a caller supplies the solution before operator Mara has to choose anything. | Make Mara choose which caller to put on air, with a cost either way. | Before: Mara follows instructions. After: she risks her brother's trust to broadcast an uncertain warning. More agency; less certainty that she is right. |
| ST-02 | Medium: SC-008 and SC-009 repeat the same accusation about their father. | Keep the stronger scene and turn the other into a practical disagreement over backup power. | Before: two explanations of resentment. After: resentment emerges through competing actions. Faster progression; less explicit family history. |
| ST-03 | Medium: Mara and named dispatcher Leena speak only about Mara's brother. No qualifying Bechdel conversation was found in the example draft. | Give Leena an independent operational goal that conflicts with Mara's broadcast plan. | Before: Leena interprets the brother. After: the women negotiate which neighborhood receives the remaining battery relay. Stronger agency and a potentially qualifying exchange; it changes how the dispatch work is portrayed and needs contextual research. |
| ST-04 | Optional production note: SC-015 describes a flooded road outside the two planned locations. | Convey the event through sound and a caller's report, or keep the exterior if it is essential. | Before: the flood is shown. After: the audience doubts an unseen report. Fewer location demands; less visual scale and direct certainty. |

These are sample findings, not universal screenplay rules. The Bechdel finding is separate from whether Leena is a compelling character; adding two lines about a battery would not establish a good revision by itself.

## First decision: one meaningful choice

The agent uses the host's native question interface if available and allowed. Otherwise it asks this in chat and waits:

> **ST-01: Should Mara make the broadcast decision?** I recommend having her choose to air the uncertain warning in SC-012. It preserves the sibling conflict and unresolved ending, while making the climax a consequence of her action. The cost is that she becomes partly responsible for a warning that might be wrong. Before: the caller tells her what to do. After: the caller gives incomplete information and she chooses. Choose **accept and apply**, **explore an alternative**, **defer**, or **keep the original**.

Illustrative writer response:

> Accept and apply, but don't make her lie. She should say the report is unconfirmed.

The agent records the actual scope of this sample response: accept the choice, preserve uncertainty in Mara's words, and avoid making her knowingly dishonest. It does not treat this as permission to change the ending or add an exterior rescue sequence.

## Second decision: the writer chooses another direction

> **ST-02: Combine the repeated family accusations?** I recommend keeping SC-008's argument and changing SC-009 to the backup-power conflict. We gain forward movement but lose the second explicit reference to their father. Choose accept/apply, explore, defer, or keep.

Illustrative writer response:

> Explore an alternative. I need both scenes, but I don't need the same argument twice.

The agent keeps both scenes unchanged while offering another specific intervention: SC-009 could show the brother silently disconnecting his own equipment to keep Mara's transmitter running. That alternative needs its own real acceptance before application. The original “explore” response did not approve it.

## Third decision: a test is a diagnostic, not a quota

> **ST-03: Give Leena an independent choice?** I recommend a practical conflict about who gets the battery relay. It could deepen her role and address the current Bechdel finding without stopping the story for a token exchange. It also introduces a real-world operational assumption we should research. Is that a direction you want to explore?

Illustrative writer response:

> Defer that until we've checked how the equipment works. Don't add dialogue just for the test.

The agent records a deferred decision, leaves the honest Bechdel finding visible, and notes a concrete research question. It does not claim the draft now passes. If the writer had already required a passing result, the revision gate would remain unresolved until a substantive accepted change and fresh assessment supported it.

## A sample decision log

This JSON illustrates state only. Copying it into a project does not establish real approval.

```json
{
  "decisions": [
    {
      "id": "ST-01",
      "scene_ids": ["SC-012"],
      "problem": "Mara receives the solution without making a consequential choice.",
      "proposal": "Mara chooses to broadcast the warning and explicitly calls it unconfirmed; preserve the unresolved ending.",
      "tradeoff": "Greater agency makes Mara partly responsible for an uncertain warning.",
      "choice": "accept",
      "evidence": "Illustrative full-draft review: SC-012 supplies instructions instead of requiring a choice.",
      "user_response": "ILLUSTRATIVE ONLY: Accept and apply, but don't make her lie. She should say the report is unconfirmed.",
      "applied": false
    },
    {
      "id": "ST-02",
      "scene_ids": ["SC-008", "SC-009"],
      "problem": "The same family accusation repeats without changing the situation.",
      "proposal": "Preserve both scenes; explore a new action for SC-009 before proposing a rewrite.",
      "tradeoff": "Less explicit explanation may demand clearer behavior.",
      "choice": "alternative",
      "evidence": "Illustrative repeated accusation on pages 8–10 and in the following scene.",
      "user_response": "ILLUSTRATIVE ONLY: Explore an alternative. I need both scenes, but I don't need the same argument twice.",
      "applied": false
    },
    {
      "id": "ST-03",
      "scene_ids": ["SC-010"],
      "problem": "Leena's role serves the brother's story; no qualifying conversation was found.",
      "proposal": "Explore an independent relay-allocation goal after researching operational plausibility.",
      "tradeoff": "More agency adds an operational assumption and may consume scarce screen time.",
      "choice": "defer",
      "evidence": "Illustrative dialogue and character review; no actual screenplay supplied in this example.",
      "user_response": "ILLUSTRATIVE ONLY: Defer that until we've checked how the equipment works. Don't add dialogue just for the test.",
      "applied": false
    }
  ]
}
```

## What application would mean

In an actual session the agent would implement only the accepted ST-01 intervention, reread the lead-in and aftermath, preserve the unresolved ending, update related scene/continuity records, and check whether any factual detail or quality finding changed. It would reopen affected workflow stages through the actual tracker and verify the revisions before setting that decision's `applied` field to true. It would not apply ST-02, ST-03, or ST-04 without the relevant actual approval or scoped delegation.

A useful meeting result might read: “Mara's accepted choice is implemented and the downstream continuity checked. Both argument scenes remain; their alternative is pending. Leena's change is deferred for research. The ending and two-location plan are preserved.” Such a result must describe real files and checks when used in production; nothing in this illustrative example is an executed change.
