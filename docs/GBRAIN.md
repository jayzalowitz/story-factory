# Optional memory for a long-running story

Story Factory already remembers your project through its files: the brief, story bible, outline, continuity notes, research ledger, review decisions, and progress receipts. You can reopen the folder and use `story-resume` without another service.

[GBrain](https://github.com/garrytan/gbrain) could add a useful second layer when a story runs across many conversations, assistants, or related projects. Our recommendation is an **optional advanced connection**, beginning with explicitly saved decisions and local keyword search. It should never become a requirement for starting a story. The initial assessment below is followed by a [bounded local pilot](GBRAIN_PILOT.md). Story Factory still does not automatically install, connect, or write to GBrain for a writer.

## What it could help you remember

A writer could ask, “Why did we remove the courtroom ending?” or “What did we promise never to change about Lena?” GBrain could retrieve an approved decision and its origin. A researcher could find the earlier note about a disputed date without rereading every session. These are potential benefits for Story Factory, not results we have measured.

GBrain documents explicit memory with provenance, corrections, withdrawal, and retrieval across connected agents. Local PGLite can start without a separate database server or embedding API. Its coding-agent tutorial describes a memory-only setup that preserves the existing assistant identity. [Memory-only tutorial](https://github.com/garrytan/gbrain/blob/51e7ba94a3ebe96062a9fef14d7072373e85c324/docs/tutorials/connect-coding-agent.md).

It would complement the project folder. A remembered claim that a draft passed review cannot establish that today's draft passed. Story Factory's source hashes, current reports, measured PDFs, and writer decisions remain authoritative.

## Claude and Codex support: what we checked

The official project includes separate native plugin manifests and connection guides for Claude Code and Codex. Both checked manifests parse as JSON. A later bounded pilot actually connected session-scoped stdio MCP to both native CLIs and observed recall, without installing plugins or persistent registration. Native summary and write checks exposed failures, so this does not establish a supported adapter. [Claude manifest](https://github.com/garrytan/gbrain/blob/51e7ba94a3ebe96062a9fef14d7072373e85c324/.claude-plugin/plugin.json), [Codex manifest](https://github.com/garrytan/gbrain/blob/51e7ba94a3ebe96062a9fef14d7072373e85c324/.codex-plugin/plugin.json).

The Claude guide offers a plugin or local MCP connection; the binary and a configured brain are still prerequisites. A local PGLite brain permits one owning process, so two independent Claude/Codex servers cannot simply open the same database simultaneously. A shared server or another supported engine is needed for concurrent access. That matters for our parallel writing teams. [Claude connection guide](https://github.com/garrytan/gbrain/blob/51e7ba94a3ebe96062a9fef14d7072373e85c324/docs/mcp/CLAUDE_CODE.md).

The Codex guide describes its own plugin distribution and trusted hooks. Upstream documents a particular observed CLI version; that is not evidence that every Codex app/version has activated those hooks. Treat installed configuration, an answering connection, and fresh-session recall as separate checks. [Codex connection guide](https://github.com/garrytan/gbrain/blob/51e7ba94a3ebe96062a9fef14d7072373e85c324/docs/mcp/CODEX.md).

## A small connection we could build later

The following is a Story Factory proposal, not an existing command or configuration schema.

1. The writer chooses memory off, explicit local memory, or an already configured shared brain. Off stays the default. A helper identifies the exact story, owner, brain, source, and permitted collaborators before any write.
2. On `story-resume`, retrieve only that story's approved memory, then read the actual project files and run the existing status checks. Conflicts go to the writer; a recalled preference never overrides their current instruction.
3. Offer to save a durable decision after the writer accepts it. Record the project ID, decision ID, approval date, source file and section, source hash, decision status, and superseded decision ID. Preserve uncertainty and distinguish author choices from researched facts.
4. Research workers return findings to the coordinator. The coordinator reconciles sources and the writer approves durable memory. Workers do not publish competing versions of story canon.
5. Before using a remembered research claim, reopen its ledger entry and primary citation. Never upgrade disputed, inferred, or invented material to verified because it appeared in memory or in several agents' summaries.
6. Correct or withdraw memory with readback. Store an audit pointer in the private project, then test recall in a new conversation. A failed or unavailable connection falls back to the folder with an honest explanation.

### Save only what the writer chooses

| Suitable after explicit approval | Keep out of the default memory connection |
| --- | --- |
| Creative constraints and durable preferences | Full transcripts, automatic session capture |
| Accepted and rejected story decisions, with reasons | Unreleased full scripts or bulk interview recordings |
| Character/setting canon tied to a specific draft | Credentials, account details, local machine configuration |
| Source-ledger pointers and uncertainty labels | Private addresses, contact lists, sensitive real-person allegations |
| Revision intent and approved continuity corrections | Raw private research, rights agreements, third-party confidential material |

A private production can make a separate, informed choice about additional material. Do not import the entire project or mix unrelated productions automatically. The public Story Factory repository and website are never destinations for a writer's private memory.

## Privacy, costs, and installation effort

A local database is not a promise that all processing stays on the computer. Connected assistants receive recalled text, and optional cloud embeddings, reranking, extraction, or synthesis can send text to their providers. Withdrawal is also different from erasure, and Markdown export is not a complete database backup. [Memory boundaries](https://github.com/garrytan/gbrain/blob/51e7ba94a3ebe96062a9fef14d7072373e85c324/docs/guides/memory-boundaries.md).

A named source organizes information; it does not isolate users who already share local files or database credentials. Use a separate brain when ownership changes, and narrowly scoped authenticated access for a shared service. Do not call a source name a confidentiality barrier. [Brains and sources](https://github.com/garrytan/gbrain/blob/51e7ba94a3ebe96062a9fef14d7072373e85c324/docs/architecture/brains-and-sources.md).

This adds installation and maintenance beyond Story Factory: Bun and the official GBrain CLI, a database location, assistant registration, restart, diagnostics, backups, and possibly shared-server operation. The upstream setup command can preview changes and keeps transcript capture and provider use separate. Review its target and existing configuration first. Do not use an unrelated npm package with the same name. Check current instructions rather than copying a stale installation recipe from this document. [Setup guide](https://github.com/garrytan/gbrain/blob/51e7ba94a3ebe96062a9fef14d7072373e85c324/docs/guides/setup.md), [official repository](https://github.com/garrytan/gbrain).

## Recommended next step

Keep today's onboarding simple. If memory becomes useful, first run a separate, explicitly authorized trial with a fictional, nonconfidential project: save one unique decision, retrieve it from Claude and Codex in separate fresh sessions, correct it, withdraw it, and verify isolation from another story. Test simultaneous access before offering it to parallel teams. Record actual tool calls and unresolved activation issues. Add paid search or background enrichment only after that trial demonstrates a benefit and the writer chooses the data and spending boundaries.

## Review record

Reviewed the official repository, memory-only tutorial, both host guides and plugin manifests, setup guide, memory boundaries, and brains/sources architecture. Snapshot: `51e7ba94a3ebe96062a9fef14d7072373e85c324`, manifest version `0.60.322.0`. Read-only inspection; no code reused, software installed, credentials changed, external processor enabled, or live integration claimed. Links above pin the reviewed revision; current upstream behavior may differ.

Later evidence: local keyless save/recall/correction/withdrawal and separate-brain routing were tested. See [pilot results](GBRAIN_PILOT_RESULTS.json). Native session-scoped recall and authenticated single-owner HTTP concurrent writes/restarts/backup restore were then exercised. Claude summary/trust handling and Codex native write approval did not pass the full acceptance gates. The automatic adapter remains deferred; see the explicit negative results in the pilot report.
