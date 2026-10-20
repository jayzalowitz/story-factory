# Optional helper teams

You can make the whole project with one assistant. Leave this section alone unless you want more control over parallel research or review.

A helper team (sometimes called a swarm) lets the assistant assign separate checks at the same time. Useful cases include researching different parts of a real story, checking continuity, giving a fresh script reading, or comparing pitches with the screenplay. It is rarely useful for a small edit. One lead assistant remains responsible for the writing and resolves disagreements.

Tell your assistant:

> Keep helper teams off. Work through the same checks yourself.

Or:

> Ask me before using helpers. If available in my current setup, propose up to two for continuity and quality review only. One round. Don't use another paid service or let helpers rewrite the script.

Or:

> Use available native helpers automatically within three workers and one round for research and review. Check what this session actually supports first, and keep one author.

The assistant saves the choice in development/teams.json. Default mode is off. Advanced controls include mode (off/ask/auto), worker limit (1–3), rounds (1–3), research sources per worker (1–20), and allowed tasks (research, continuity, quality, package-review). Nested teams and new paid providers remain disabled. Changes outside these supported limits need a separate concrete setup decision.

A paid plan does not guarantee teams, web research, concurrent capacity or remaining allowance. The assistant checks the actual exposed tools. If unavailable, it does the same passes sequentially and says so. Helpers can use your existing plan allowance; the system cannot enforce a dollar budget when the provider exposes no usage meter. No API key, second model subscription or external service is silently added.

Workers receive bounded assignments and separate notes folders. They do not edit the script simultaneously. The lead records the actual team, what it checked, findings, disagreements and limits in development/team_plan.json and team_report.md. Same-model reviewers are not independent human experts. The full operating instructions are [TEAMS.md](../skills/story/references/TEAMS.md).

## Optional memory, investigated separately

[GBrain assessment](GBRAIN.md) explains a possible future connection for approved decisions and continuity across sessions. Nothing is installed or enabled. The project folder already supports resuming without it; this is not part of first-time setup.
