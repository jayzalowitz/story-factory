# Research that serves the story

Read `COMMON.md` before running a command. Use this guide with `story-research` and `story-truth`, the craft guidance in `MASTER_PROMPT.md`, and the staged tracker in `WORKFLOW.md`. Research produces usable evidence and dramatic possibilities; it does not outsource the writer's decisions to a pile of links.

## Choose what promise the film makes

Save the choice in `research/source_mode.json`, and explain it in ordinary language in the brief. Do not infer a stronger truth claim from an exciting seed.

| Mode | Audience promise | How to work |
| --- | --- | --- |
| `original` | An invented story; researched details may make its world credible. | Research relevant work, places, communities, period details, and practical constraints. Do not invent a real person's involvement. Truth review applies to factual assertions and marketing claims, not to whether invented events happened. |
| `based-on` | Identifiable events or people provide the story's substantial factual foundation. | Establish an evidence-backed chronology and relationship map before locking structure. Trace consequential events and allegations to evidence. Record inventions, compression, composite characters, and disputed interpretations explicitly. |
| `inspired-by` | A real seed informed an independently invented story. | State the precise seed and how the invented story departs. Separate researched context from invented plot. Changing names alone does not establish that recognizable people have become independent fictional characters. |

Use `intended_claim` for the actual proposed wording, such as “An original drama informed by research into community radio.” Treat “based on a true story” and “inspired by true events” as proposed audience-facing statements to assess, never as automatic certifications. A change of mode changes the brief, packaging language, research needs, and relevant workflow receipts.

## Start with a bounded research question

Read existing sources and the user's guidance first. Record scope, subject, period, geography, unanswered dramatic questions, supplied source material, and useful exclusions in `research/plan.md`. Preserve the user's actual restrictions: events to keep, people to protect, inventions allowed, tone, and source material they control. Ask about a consequential missing choice; make routine research choices autonomously.

Read TEAMS.md and development/teams.json first. With teams off (the default), do these passes sequentially. When teams are enabled, set the budget to one coordinating agent plus at most three workers, at most ten candidate sources per worker, and one initial pass. Count all nested workers against that same cap. A worker may ask for further research; it must not recursively spawn an unbounded team. Prefer a small number of strong sources to a search-result dump. Record the actual count and unresolved gaps. Exceed the budget only with a recorded reason and the user's applicable spending/tool authorization; stop and ask before new paid services or a material expansion.

Invoking the research command authorizes ordinary web research using tools already available to the current approved host. When teams are enabled, use Codex's native subagents when running in Codex and Claude's native subagents when running in Claude, if that capability is actually exposed. Do not launch another model CLI, API, external agent service, or new processor to simulate delegation. Do not upload private manuscripts or sensitive source material to a new service. No outreach, interviews, purchases, account creation, or publication is authorized by this command.

## Delegate distinct questions, then reconcile

Create an assignment manifest before delegation. Give each worker its own output directory and bounded task; they may read shared files but must not edit the master ledger, screenplay, or another worker's files.

| Worker | Question | Exclusive write directory |
| --- | --- | --- |
| Chronology | What happened when? Which turning points are established, disputed, or unknown? | `research/workers/chronology/` |
| Relationships | Who knew whom, what did each person want, and whose account is missing? | `research/workers/relationships/` |
| Context and challenge | What social, professional, cultural, or material constraints matter? What evidence contradicts the leading interpretation? | `research/workers/context/` |

Use only the host's documented native tools. Example assignment text, not an executable tool call:

> Research only the chronology of [subject] during [period] using up to ten candidate sources. Prefer original records and clearly identify later retellings. Write notes.md and candidate_claims.json only inside research/workers/chronology/. Include source URLs, exact locations, access dates, relevant short quotations or paraphrases, uncertainties, contradictions, and dramatic implications. Do not invent evidence, write screenplay scenes, edit shared files, contact anyone, spend money, or spawn further agents. Return a concise findings report and actual files written.

Adapt the question and exclusive directory for each worker. If native delegation is unavailable, state “Research ran sequentially in this host; no independent subagents were available,” and perform the same three passes in the same separate directories. Never fabricate workers, conversations, tool calls, independent agreement, or independent review. Running several roles in one context is useful but remains one agent's work.

The coordinating agent reads every report, opens the decisive sources, removes duplicate or derivative citations, checks apparent contradictions, and owns the final claims ledger. Three articles quoting one memoir remain one underlying account. A worker's confidence is a proposal until reconciled. Keep disagreement visible rather than voting it away.

## Make sources and claims inspectable

Write `research/claims.json` as an object with `sources` and `claims` arrays. Use stable IDs such as `SRC-001` and `CLM-001`; never renumber IDs already used in scenes. The illustrative fixtures in `examples/research/` show the shape only and provide no evidence.

Every source includes `id`, `url`, `title`, `author`, `published`, `accessed`, `kind`, and `locator`. Use ISO dates where known; use null for unknown dates instead of guesses. A locator identifies a page, archival identifier, section, paragraph, transcript timestamp, or stable heading. A bare homepage or search snippet is not an adequate locator. For private/offline material, use a local archive reference as `url`, record access constraints, and do not publish confidential text. Distinguish primary record, contemporaneous report, later scholarship, memoir, interview, and derivative retelling. A primary source can still be mistaken, self-serving, incomplete, or forged; provenance is evidence, not truth by itself.

Every claim includes `id`, `text`, `status`, `source_ids`, `scene_ids`, and `notes`. Recommended extra fields are `kind` (`fact`, `inference`, `quote`, `disputed`, or `invented`), `confidence` (`high`, `medium`, `low`, or `not-applicable`), `evidence` (source ID, exact locator, supporting paraphrase or short excerpt), `contradictions`, and `public_use`. Keep quotations exact, brief, and attributed; distinguish words actually spoken from reconstructed dialogue. A citation to the general event does not verify dialogue, motive, private thought, or an invented meeting.

| Claim status | Meaning |
| --- | --- |
| `verified` | The precise assertion is supported by evidence the coordinator actually inspected; record its limits. This is a research judgment, not absolute certainty. |
| `disputed` | Credible accounts conflict or the evidence permits materially different conclusions. Preserve the competing source IDs and interpretations. |
| `unverified` | The assertion has not been established, including plausible details and inaccessible sources. |
| `inference` | A reasoned interpretation grounded in stated evidence; explain the reasoning and alternatives. |
| `invented` | A deliberate creative choice. Do not supply a citation as though it proves the event occurred. |

Do not upgrade missing evidence to invention silently. “We have no record” differs from “this did not happen.” Record search/access limits. Repeated claims do not become corroborated merely through repetition. Log retractions or source corrections and reopen affected work.

Write `research/chronology.md`, `relationships.md`, `context.md`, and `open_questions.md`. Each factual entry links to claim IDs. End each file with dramatic opportunities and constraints: what someone could do, what it would cost, and what remains uncertain. Avoid unsupported psychological diagnoses and tidy motives presented as biography.

## Connect evidence to scenes and choices

Maintain `research/scene_traceability.md` with one row per relevant scene: scene ID; claim IDs; factual anchor; invention or compression; uncertainty; effect on the audience's understanding. Match the screenplay's stable scene IDs. Include reconstructed conversations, composites, reordered events, altered relationships, and invented endings in `creative_departures` in `source_mode.json`. Each departure should describe its reason, affected scenes, and whether it materially changes the real person's role or the event's meaning.

A based-on scene can contain invention. Make that invention legible to the writer and reviewer without burdening the screenplay with footnotes. An inspired-by scene need not prove fictional action occurred; check whether identifiable real people are being assigned unsupported conduct and whether promotional copy promises more factual fidelity than the story delivers.

## People, source material, and publication

For historical subjects, check anachronism, translation, provenance, competing accounts, and whether later mythology has replaced contemporary evidence. Death does not make private sources public or remove other people's interests. For living people and identifiable survivors, take particular care with allegations, intimate details, vulnerability, privacy expectations, and the difference between documented conduct and invented misconduct. Record specific unresolved issues and practical choices, not generic warning paragraphs.

Record source-material ownership, licenses, permissions actually obtained, and unconfirmed assumptions in `research/source_material.md`. Publicly available material is not necessarily free to adapt; underlying events and someone's protected expression are different things. Do not copy distinctive scenes or lengthy prose from a book because it describes real events. Identify a concrete question for qualified advice if the proposed use depends on uncertain rights, privacy, or allegations. This process does not provide legal clearance, and it does not require every fictional story to pass a ceremonial legal checklist. Continue authorized creative work with visible uncertainties; hold a specific unsupported public claim or proposed use when necessary.

## Review and stop honestly

Before structure locks for `based-on` or `inspired-by`, run `story-truth` and supply the tracker’s conditional real-story gate with substantive research and truth-review artifacts. Follow the actual tracker interface; never invent a completion command or bypass a failing gate. For `original`, document the mode and review only applicable factual claims; do not manufacture biographical obligations. Recheck after material scene changes and before packaging or publication. A source edit that changes the meaning of a scene invalidates its earlier review.

`research/truth_report.md` records mode, scope actually checked, evidence read, scene findings, proposed repairs, unresolved issues, and `Verdict: PASS` or `Verdict: REVISE`. PASS means the checked story's stated truth promise is supported at its intended level, departures are explicit, and no consequential contradiction is concealed. It does not mean legal clearance, exhaustive research, publication approval, or that every depiction is factual. Missing decisive evidence yields REVISE or a narrower honest promise, not a fabricated citation. Close the research pass with a usable summary and the most valuable next questions; research should improve a story, not postpone it indefinitely.
