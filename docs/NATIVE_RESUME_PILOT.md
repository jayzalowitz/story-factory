# Bounded native session resumption

Actual Claude and Codex CLI sessions were reopened against their existing short-screenplay projects. Each ran installed resume guidance and the workflow status command, with session-scoped fictional-memory MCP available. This was a small continuation task with no screenplay edits or generation, not a repetition of the original writing trial.

| Host | Evidence | Limit |
| --- | --- | --- |
| Claude Code 2.1.42, Haiku 4.5 low effort | Existing timed-out writing session reopened; native Skill invoked story-resume; actual status and MCP recall returned; process exited 0 in 25.24 seconds; manuscript hashes unchanged | Final summary contradicted `discover: NEXT` and conflated a separate memory fixture with story canon. Clean return is proven; reliable status/source summarization failed. |
| Codex CLI 0.162.1, gpt-6-luna low effort | Existing writing thread reopened; actual workflow status and MCP recall returned; process exited 0 in 22.97 seconds; manuscript hashes unchanged | Final correctly reported discovery next and quoted the exact fixture. No account-allowance reset, GUI onboarding or full-feature resumption was tested. |

The earlier Claude writing timeouts remain failures. A clean bounded follow-up does not retroactively turn a timed-out writing trial into complete native creative delivery. No further native call was made to verify subsequent instruction repairs.

A second bounded memory call in each host exposed additional write limitations: Claude's correction remained contested and old D1 active; Codex's native approval gate denied remember before mutation. The coordinator stopped at two calls per host. These are recorded negative outcomes, not reasons to keep generating until a pass appears.

[Memory pilot results and usage](GBRAIN_PILOT.md) disclose the actual operations, return times, provider-reported counters, limitations and deferred-adapter decision. The [sanitized machine-readable record](GBRAIN_PILOT_RESULTS.json) preserves selected result fields. Raw events, private session identifiers, paths and credentials are excluded.
