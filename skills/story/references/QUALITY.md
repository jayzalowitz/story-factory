# A screenplay quality review that can say no

Read the actual draft. The treatment, page count, number of revisions, and formatting quality cannot establish whether the film works. Use stable scene IDs, short precise excerpts, and consequences for the audience. Mark absent evidence unassessed. Avoid self-awarded numeric scores with false precision.

| Dimension | What to test | A useful failure signal |
|---|---|---|
| Dramatic spine | A specific pursuit and opposition persist across the film | Each act offers another mood without advancing the same struggle |
| Agency | Choices change later options and cost something | The protagonist receives information while others cause every turn |
| Causality | Scenes change a condition that matters downstream | Scenes can be shuffled without altering anything |
| Escalation and pacing | Pressure develops and the middle changes the problem | Three scenes repeat the same refusal |
| Character independence | Supporting people want things and make consequential decisions | Women, friends, workers, or antagonists exist only to explain the lead |
| Relationships and voices | Each relationship exposes a different conflict; tactics and language differ | Three partners repeat admiration, recognition, rejection |
| Subtext and action | People act, evade, resist; behavior carries meaning | Everyone explains the theme; action is unfilmable inner summary |
| Emotional range | Specific life, wit, warmth, appetite, competence or fear create contrast | Unbroken solemnity substitutes for depth |
| Form and chronology | Point of view and time shifts are legible and necessary | The viewer repeatedly re-orients without learning anything new |
| Ending and title | The final choice pays a price established earlier | The ending is imposed by a speech or a sudden invented solution |
| Production logic | Locations, cast, effects, period and action fit the intended scope | The package claims a contained production while the script needs spectacle |
| Truth and permissions | Real claims, inventions and sources are separated | A composite is described in the pitch as a documented historical person |

For each dimension record strong/revise/unassessed, scene evidence, implication, and a concrete next action. Conclude READY only when no unresolved issue defeats the requested draft's core design. Preserve smaller limitations and actual user-accepted tradeoffs. READY does not mean a professional reader agreed, a financier will invest, or historical/legal review is complete.

## Bechdel assessment

Use the named-women variant: two named women, a conversation between them, and a subject other than a man. This criterion is described by [Bechdel Test Movie List](https://bechdeltest.com/); it is a narrow representation diagnostic. It does not measure feminism, character depth, narrative craft, or whether an intentionally limited-cast story should exist.

Confirm women from the work or explicit roster, not guessed names. A qualifying exchange must actually address each other about a non-man subject. Two names in a cast list are insufficient. A conversation may include references to men and still contain a separate substantive non-man exchange; explain what qualifies. Talking about a woman, their own work, a practical conflict, politics or an impersonal problem can qualify when it is truly the exchange's subject rather than a proxy discussion of a particular man.

Report PASS, FAIL or UNCLEAR with scope. For a full-draft FAIL, inspect the full draft. For an excerpt, report only that excerpt's result, and state that a full-film verdict remains unknown. A qualifying excerpt provides evidence of a qualifying scene, not proof of the rest of the screenplay's quality. If names, gender, addressee or subject are ambiguous, record UNCLEAR and the ambiguity. Do not invent a count or infer offscreen dialogue.

Then ask the harder independent questions: do women have goals beyond the lead, make decisions with consequences, disagree for their own reasons, and affect the film? Who else is reduced to a symbol? Avoid token repairs or a universal quota. A dramatically necessary scene can improve both agency and the test result, but passing alone is not enough.

## Review receipts

Use `python3 scripts/story_check.py fingerprint` to identify the actual screenplay version. Store that value as draft_sha256 in both development/quality.json and development/bechdel.json. Recheck after ANY screenplay change. The corresponding Markdown reports preserve scene evidence, judgment, limitations and repair priorities. The mechanical quality command checks currency and report completeness; it is not an automated literary critic or gender classifier.
