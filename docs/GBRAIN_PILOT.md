# Optional memory: a bounded local pilot

**Local memory, native recall in both hosts, and a single-owner shared HTTP service were exercised. Native write and summary-fidelity checks did not all pass, so the Story Factory adapter remains deferred and memory stays off by default.** The project folder remains the source of truth. The follow-up used exactly two bounded native calls per host; no new creative draft was generated.

The initial lifecycle pilot used only the fictional *Glass Orchard*; the follow-up used separate explicitly fictional native-host and shared-service fixtures. No screenplay, interview, real-person research, automatic session capture, embedding model, hosted database, or new model service was supplied to the memory store. The first lifecycle trial ran only the official upstream CLI locally and requested no model call. The authorized follow-up used existing native sign-ins for four short inference calls and ephemeral local OAuth clients for the HTTP proof. Usage disclosures below do not establish billed subscription cost.

## Revisions and boundaries

- Official repository revision: [`51e7ba94a3ebe96062a9fef14d7072373e85c324`](https://github.com/garrytan/gbrain/tree/51e7ba94a3ebe96062a9fef14d7072373e85c324), version `0.60.322.0`.
- A temporary source checkout and dependency installation stayed outside the distributed toolkit. Upstream code is not copied into Story Factory.
- The existing Bun `1.3.11` was refused by upstream's `>=1.4.0` runtime gate. A separate official Bun `1.4.3` archive was used for the trial, without changing the global runtime.
- Each process received a fresh environment containing only its PATH and an isolated absolute `GBRAIN_HOME`. Bun's environment-file loading was disabled. No user assistant configuration or credentials were modified.
- A new PGLite brain was initialized with `--no-embedding`; `memory.auto_writeback` was set to `off` and search mode to `conservative`. No harness was registered. No service was exposed.

## Actual operations and observed results

The following uses `gbrain` as shorthand for running the checked-out `src/cli.ts` through the isolated Bun with `--no-env-file`. It is a record of the pilot, not a recommendation to install an unreviewed global package. All completed operations below exited `0`.

| Operation | Observed result |
| --- | --- |
| `init --pglite --no-embedding` in a new canonical directory outside Git | Schema v262 initialized; 257 migrations applied. Upstream separately reported five pending setup migrations. The explicit memory operations below nevertheless worked. |
| `config set memory.auto_writeback off` | Off recorded in file and database planes. |
| `config set search.mode conservative` | Conservative search recorded. |
| `remember` fictional D1 with entity `projects/glass-orchard` and explicit provenance | Fact `1` inserted and committed. |
| A separate `recall projects/glass-orchard --json` process | Exactly D1 returned with its provenance. |
| `remember` fictional D2 with `--replaces 1`, the same entity, and correction provenance | Fact `2` committed with `status:superseded`, `superseded_fact_id:1`, `replaced_by_caller:true`. |
| A separate recall after correction | Only current D2 returned; old D1 was absent from active recall. |
| `recall projects/copper-harbor --json` | No facts returned. This tests entity routing, not access control. |
| Two recall CLI processes started concurrently against the same local brain | Both exited `0` and each returned the same current D2. This is a narrow concurrent-read observation, not a shared-server or concurrent-write guarantee. |
| Recall of the same entity in a separately initialized brain | No facts returned. This tests separate database selection; local file access remains a separate boundary. |
| Active separate-production marker saved and recalled in the second brain, then queried in the first | Second brain returned its marker; first brain returned no facts for the same entity while the marker was active. The second marker was then withdrawn. |
| `forget 2 --reason ... --json` | Withdrawal committed with `expired:true`. |
| A separate recall after withdrawal | No active facts returned. Withdrawal does not erase historical records or backups. |

The test phrases were “the bridge stays closed” and its approved correction “the bridge opens at dawn,” both carrying marker `amber-orbit-7319`. Provenance named fictional decisions D1/D2 and their intended project-file locations. Those pointers were provenance text in a test, not evidence that an actual manuscript passed review.

The machine-readable [pilot record](GBRAIN_PILOT_RESULTS.json) preserves the actual command arguments and selected result fields. It excludes temporary machine paths, installation logs, and unrelated configuration.

## What this shows

Explicit, keyless, local memory can retain a selected decision across processes, replace its current version with provenance, and withdraw it from active recall. That is a useful reason to continue evaluating an optional memory connection for long-running stories. The keyless mode reported degraded deduplication: exact duplicates can be detected, but paraphrased duplicates and withdrawals are not semantically resolved. Never promise that forgetting one sentence removes every rewording.

Project selection must be deliberate. An entity or source label is not a confidentiality boundary for callers with the same brain access. Separate productions with different owners require separate brains or a properly authenticated and tested shared service. See upstream's [memory boundaries](https://github.com/garrytan/gbrain/blob/51e7ba94a3ebe96062a9fef14d7072373e85c324/docs/guides/memory-boundaries.md).

## Setup friction actually encountered

The first attempt stopped at the Bun version gate before initialization. A later attempt placed the content directory within an existing Git worktree; upstream refused to claim that parent repository. Another attempt used macOS's symlinked `/var` path; upstream required a canonical directory whose parents are real directories. Resolving the temporary directory to its canonical location outside Git allowed initialization. These failures are reasons to keep this out of beginner onboarding until a setup helper handles them.

## Authorized follow-up: actual native connections

Both existing writing sessions were reopened with session-scoped MCP configuration, with no global registration or hooks. The native model probes used Claude Haiku 4.5 at low effort and Codex's locally advertised `gpt-6-luna` at low effort. Each had a 90-second cap; all four returned before it. Source hashes were unchanged. The exact private session IDs, local paths, credentials and raw transcripts remain outside this repository.

| Probe | Actual evidence | Acceptance result |
| --- | --- | --- |
| Claude resume + recall, 25.24s | Resumed the previously timed-out writing session; invoked native `story-resume`, read its procedure, ran workflow status and called native MCP `recall` | Connection/tool activation passed. Summary fidelity failed: the tool said `discover: NEXT`, but the final answer called discovery complete and premise next. It also substituted manuscript canon for the separate fictional fixture rather than quoting its marker. |
| Claude correction + withdrawal, 27.73s | Called native recall, remember with replaces/provenance, recall, forget and recall | Requested lifecycle acceptance failed. The assistant labeled document-derived D2 `tool_output`; GBrain stored it as an untrusted contested challenger rather than silently replacing D1. D2 was withdrawn, but D1 remained active. The final answer acknowledged D1 yet incorrectly called the test complete. |
| Codex resume + recall, 22.97s | Reopened its existing native session, ran workflow status and called native MCP recall | Correctly reported discovery as next and quoted the exact fictional marker and fact ID. This is a bounded resume/recall observation, not a new full screenplay trial. |
| Codex correction request, 14.30s | Recalled D1 and attempted native remember | The host required approval under the chosen `never` policy, so the write was blocked before reaching GBrain. The assistant accurately stopped and reported the test incomplete. Correction/withdrawal were not exercised through Codex. |

The fixture was explicitly fictional and separate from each manuscript. Its successful retrieval must never become a story-canon claim. A tool returning text, a model quoting that text correctly, a correction committing, and a trustworthy final summary are separate acceptance checks.

Claude exposed per-run native usage: first probe 17 input, 54,289 cache-creation, 160,171 cache-read and 561 output tokens; second 32 input, 58,852 cache-creation, 340,830 cache-read and 796 output tokens. Its CLI reported USD 0.08771035 and 0.112122 respectively; these are provider-reported estimates, not measured charges against a subscription. Codex reported cumulative resumed-session aggregates of 740,366 input / 616,448 cached / 5,837 output after recall, and 1,137,773 / 1,010,304 / 6,304 after the write probe. Those fields include prior session activity and must not be summed as independent probe usage. Exact isolated new-call Codex cost and weekly allowance impact remain unknown.

No inference retry followed the two-call-per-host cap. The earlier creative timeouts and scope failures retain their original verdicts. Updated resume instructions are a preventive change; no additional native run has verified that change.

## Single-owner HTTP concurrency, authorization and recovery

This follow-up requested no model inference. One official GBrain HTTP process owned a fresh PGLite database and listened only on loopback. Three explicitly registered OAuth clients used 600-second access tokens: two read/write clients and one read-only client. Dynamic registration stayed off. No token or secret appears in the distributed results.

- Two independent HTTP MCP clients submitted fixture writes simultaneously. Both acknowledged committed facts, and fresh recall returned both.
- A correction replaced fact 1 with fact 3. Readback returned corrected 3 and independent 2, excluding old 1. Withdrawing 3 left independent 2 active.
- An invalid token received HTTP 401. The read-only client was denied remember with `insufficient_scope`. An unrelated entity returned no fixture facts; entity names still do not provide access control.
- A graceful owner restart retained fact 2. After an acknowledged committed recovery fixture, the owned process was killed abruptly and restarted; recall retained that fixture. This tests acknowledged-write durability and owner-lock recovery, not interruption during an unacknowledged transaction.
- Official `backup create` produced a private 0600 archive. Official `backup restore` into a separate new-brain directory succeeded, and recall returned the recovery marker. Upstream detached ownership/publication and revoked restored credentials. This was a same-machine independent restore, not an off-host disaster recovery drill.
- The original test clients were revoked. The server stopped and the port was verified closed. Fictional databases and archives remain privately retained as evidence.

Two local harness errors occurred before service testing: an unsupported registration flag and a recorder argument collision. Both were corrected from their exact errors; these were local harness repairs and made no model calls. An abandoned pre-service test database later refused cleanup access with a PGLite WASM initialization error. Its one client remains in that offline private database; no server was ever started for it and no credential was logged or distributed. No repair was attempted. The successful run's three clients were revoked. The complete successful run passed explicit result assertions for simultaneous commits, replacement, withdrawal, scoped refusal, both restarts, archive permissions and restored recall.

## Setup migration classification

`apply-migrations --list --json` reported schema v262 managed in-process, zero ordinary pending/wedged migrations and five `pending_fresh_install` setup entries: 0.11.0 (background minions), 0.14.0 (shell jobs/autopilot), 0.22.4 (frontmatter guard), 0.28.0 (takes), and 0.53.0 (shared content/skills). These are host/background setup work, not five missing SQL migrations. Broad application can walk or rewrite existing assistant host integrations, beyond this isolated pilot, so it was not run. No supported complete installation is claimed.

## Decision and remaining limits

The transport/storage POC succeeded within the stated single-owner scope. The native fidelity and write-approval gates exposed concrete blockers. Story Factory therefore does not activate or distribute an automatic memory adapter. Memory remains off by default, and project files plus current hash-based receipts remain authoritative.

A future adapter must present provenance and trust/contested states, distinguish fixture or imported text from writer instructions, refuse to upgrade stale approvals, verify correction/withdrawal readback, handle native approvals explicitly, and continue folder-only when memory is unavailable. A fresh-conversation memory journey distinct from these resumed threads, an actual unavailable-connection assistant journey, complete host setup, cross-user production authorization and off-host restore remain untested. Closing a bounded experiment with a negative result is not a supported-integration claim.

The machine-readable [pilot record](GBRAIN_PILOT_RESULTS.json) includes the original lifecycle and sanitized follow-up results. [Native resume details](NATIVE_RESUME_PILOT.md) separate clean process completion from summary accuracy.
