# Why this is a writing process, not one giant chat prompt

A film project grows: screenplay, research, alternate ideas, notes, rewrites, synopsis and pitches. An AI assistant has a limited amount of information it can consider at once, called its context window. Its answer also has a length limit. A long conversation can reach those limits, lose access to earlier details, or summarize away something you wanted preserved.

A more capable model can still have a finite window: reasoning ability and how much text it can hold at once are different limits. The visible chat history is not proof that every earlier message is still being considered in full. Exact behavior varies by model and app. [OpenAI's context explanation](https://developers.openai.com/api/docs/guides/conversation-state), [Anthropic's context explanation](https://platform.claude.com/docs/en/build-with-claude/context-windows).

Story Factory gives the project a durable record: the manuscript, story bible, scene map, approved decisions, sources, revision notes and current checks. The assistant works in stages, reads the files relevant to that task, and saves what changed. At useful stopping points it saves a checkpoint: what is finished, what remains unread or unresolved, and the next action. A later session uses `/story-resume` in Claude Code or `$story-resume` in Codex to reload the relevant records. It does not need to remember every previous chat message.

This manages context; it does not give a model infinite memory or guarantee perfect consistency. The assistant must actually consult the files. Summaries and optional memory notes cannot replace reading the draft or override your approved decisions. A whole-draft review must cover every scene of the same current version. It can read that draft in tracked sections, then check the relationships between them; summaries cannot stand in for unread scenes. A sample read is always labeled as a sample.

## The loop: write, diagnose, repair, recheck

1. Develop a clear dramatic promise and characters with independent wants.
2. Write complete scenes and a complete draft.
3. Read the entire current draft and identify important weaknesses with scene evidence.
4. Repair the causes: weak choices, repetitive relationships, missing consequences, unclear chronology or an unearned ending.
5. Recheck changed scenes, their setups/payoffs, continuity and the current version's quality reports. Structural changes may require another complete read.
6. Create only the selected materials, align them to the revised screenplay, build actual PDFs and inspect every delivered page.

The loop is bounded. The assistant prioritizes consequential changes, checks whether its repairs worked, and stops when further changes would be cosmetic or create new problems. It records unresolved weaknesses and any blocked stage honestly. This avoids spending your allowance on endless reviews; reaching the end of a repair round does not automatically make the draft ready.

## What the gates check

| Gate | Evidence | What it cannot certify |
|---|---|---|
| Story and craft | Full-draft coverage, scene-specific findings, meaningful revisions, protected strengths and remaining risks | That an audience, professional reader or financier will agree |
| Bechdel assessment | Whether two named women actually converse about something other than a man; PASS, FAIL or UNCLEAR with cited scenes | Character depth, feminism or artistic quality. The actual result is always reported. Passing is required only if you chose that goal. |
| Agency and continuity | Independent character goals, consequential choices, causal scenes, timeline and setup/payoff checks | That every human interpretation will agree |
| Research and adaptation | Current sources, facts/disputes/invention, source-to-scene mapping, fidelity decisions and final truth-label audit | Rights clearance or independent historical corroboration where none exists |
| Current version | Saved version identifiers tie reports to the manuscript and source settings they actually reviewed; edits can make them stale | That a declared review was competently performed |
| File delivery | Real PDF builds, measured page counts, readable one-page pitches, all-page visual records and an inventory of the selected editable source files | A finished film, commercial success, or perfect proofing |

Every complete run includes the applicable checks: research and adaptation depend on your source material, and file checks cover the materials you selected. You do not need to know the specialist commands. Software checks that the required records exist and match the current version. The AI reader supplies the editorial judgments, and you make creative decisions. Mechanical checks never decide whether art is good.

For the exact assistant protocol, see [context guidance](../skills/story/references/CONTEXT.md), [quality rubric](../skills/story/references/QUALITY.md) and [delivery standard](../skills/story/references/DELIVERY.md). The original feature's 116 historical studio cycles are not a recommended quota; structural insight comes before repeated line polishing.
