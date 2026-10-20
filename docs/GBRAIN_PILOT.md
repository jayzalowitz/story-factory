# Optional memory: a bounded local pilot

**The local memory lifecycle worked. Native Claude/Codex activation is still unverified, so Story Factory does not enable or require a memory adapter.** The ordinary project folder remains the source of truth and the beginner path needs no changes.

This pilot used only the fictional *Glass Orchard*. No screenplay, interview, real-person research, credentials, automatic session capture, embedding model, hosted database, or new model service was supplied. It ran the official upstream CLI locally. Subscription usage and provider spend were not measured; no model API call was requested by these commands. This is not a claim of a measured zero-cost production integration.

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

The first attempt stopped at the Bun version gate before initialization. A later attempt placed the content directory within an existing Git worktree; upstream refused to claim that parent repository. Another attempt used macOS's symlinked `/var` path; upstream required a canonical directory whose parents are real directories. Resolving the temporary directory to its canonical `/private/var/...` location outside Git allowed initialization. These failures are reasons to keep this out of beginner onboarding until a setup helper handles them.

## Remaining acceptance gates

1. Connect one approved test brain to native Claude and Codex through session-scoped or otherwise isolated configuration; start fresh conversations and demonstrate actual tool discovery and recall. Plugin manifests and successful CLI calls do not prove this.
2. Repeat correction and withdrawal through those actual assistant connections, with explicit writer approval and project-file decision receipts.
3. Test a supported single-owner/shared-server configuration under simultaneous clients, including writes, interruption, recovery, and authorization. Two successful CLI reads do not establish that two independent long-lived PGLite owners are safe.
4. Demonstrate that an unavailable memory connection falls back to authoritative project files without blocking writing or upgrading stale review claims.
5. Reconcile the setup migrations reported by upstream before presenting this as a supported installation.

To conserve the user's assistant allowance, this pilot made no additional native model inference runs. No native host activation, long-lived shared service, recovery, or cross-user authorization result is claimed. Those open gates keep the adapter deferred and memory off by default.
