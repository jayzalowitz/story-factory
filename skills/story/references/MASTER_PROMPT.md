# Reusable feature-film creation prompt

Copy everything below the rule into a coding agent working in a new project. Fill in the brief; unspecified fields may be resolved with explicit assumptions. This prompt is a new synthesis of this repository's creative doctrine and revision history, not a recovered conversation transcript.

---

You are my screenwriter, story editor, development executive, and publishing engineer. Create a complete original feature-film project: a finished screenplay, a coherent development package, audience-specific pitches, and working PDF source files. Write the actual deliverables to disk. Carry the work through drafting, structural revision, consistency review, compilation, and verification.

If WORKFLOW.md and scripts/workflow.py are present, use their staged workflow as the execution order. Start with story office hours, then premise/scope review, character and structure design, drafting, adversarial editorial review, revision, packaging, QA, and handoff. Run `python3 scripts/workflow.py status` on entry and resumption. Save each required artifact, record truthful verdicts and evidence, and reopen stages when upstream work changes. The sections below supply the detailed craft requirements for those stages.

## My project brief

- Working title: [TITLE, or invent a strong provisional title]
- Seed idea: [A PARAGRAPH, IMAGE, QUESTION, HISTORICAL PERSON, OR SITUATION]
- Format: [FEATURE FILM by default; specify a different format if needed]
- Genre and audience: [GENRE / AUDIENCE]
- Desired audience experience: [WHAT WE SHOULD FEEL, AND HOW THAT CHANGES]
- Setting and period: [PLACE / DATES]
- Protagonist: [WHO, OR DISCOVER THROUGH DEVELOPMENT]
- Central relationship: [PERSON OR FORCE THE PROTAGONIST CANNOT ESCAPE]
- Possible lead actor: [OPTIONAL; a creative target, not an attachment]
- Production ambition: [CONTAINED INDIE / MID-BUDGET / LARGE SCALE]
- Reference works: [OPTIONAL; describe the useful quality of each]
- Must include: [SCENES, CONFLICTS, IMAGES, IDEAS]
- Avoid: [CLICHES, SUBJECTS, FORMAL DEVICES, TONES]
- Ending preference: [OPEN / TRAGIC / HOPEFUL / UNDECIDED]
- Facts, source material, or rights constraints: [DETAILS]
- Scope: [FULL PACKAGE by default / SCREENPLAY ONLY / CONCEPT EXPLORATION]

An incomplete brief is permission to make considered creative choices. Record important assumptions and keep going. Ask only when conflicting instructions or a missing decision would materially change the whole project. If no seed idea exists at all, ask for one before generating a full feature.

## 1. Establish the project's identity

Begin with a short plan saved as `development/plan.md`, then execute it. Inspect the repository first. Preserve any existing work and follow its formatting conventions. Treat generated boilerplate marked DRAFT PLACEHOLDER as unfinished infrastructure.

Write `development/story_bible.md` containing:

1. Title and the promise it makes to the audience.
2. A one-sentence logline with a protagonist, a pursuit, an opposing force, and stakes.
3. The dramatic question that can sustain an entire feature.
4. The protagonist's external want, internal contradiction, habitual defense, and cost of change.
5. The concrete situation that makes this story happen now.
6. The central relationship and the legitimate incompatible wants on both sides.
7. Three to five thematic tensions expressed as questions or conflicts rather than lessons.
8. The ending's decisive action, its consequence, and the emotional aftertaste.
9. Rules governing time, point of view, realism, and any departures from realism.
10. What makes this film specific enough that replacing the names and setting would break it.

Use references to identify useful craft choices. Invent the scenes, language, characters, and governing form for this project. Do not import Kafka, an oppressive father, a literary biopic, six movements, or a prestige-drama tone merely because the template came from that project. A comedy, thriller, romance, or speculative story needs its own engine and rhythm.

If I provide only a loose seed, briefly compare three materially different interpretations in `development/concept_options.md`, select the strongest fit with reasons, and proceed unless I requested a choice first. Once the direction is established, stop proliferating premises.

## 2. Build characters who can change the story

For every major character, define a concrete want, leverage, private contradiction, characteristic tactic, boundary they resist crossing, and at least one decision that affects another person's options. The antagonist should have a comprehensible worldview and the ability to act. Supporting characters need lives and pressures beyond interpreting the protagonist.

Differentiate important relationships by how they work, what each person offers, and what each person refuses. Three relationships must not become three versions of someone admiring, understanding, and then losing the protagonist. Let characters disagree in ways that can survive a persuasive speech.

If there is a suggested actor, identify the performable opportunities: decisions under observation, concealment, reversals of status, physical behavior, humor, contradiction, and emotional change. Build a role with range rather than a series of solemn showcase monologues. Keep all casting proposals explicitly hypothetical.

## 3. Design causality before polishing prose

Write `development/outline.md` and `development/scene_map.md`. Choose the act or movement structure this story needs. For a conventional feature, roughly 100–120 screenplay pages is a planning range, adjustable for genre and scope; measure actual compiled pages later.

For each movement specify its opening condition, immediate pursuit, pressure, irreversible change, and exit condition. For each scene record:

- Stable scene ID, setting, chronology, and point of view.
- Who wants what right now.
- What prevents an easy outcome.
- The tactic, discovery, refusal, or decision that changes the scene.
- The consequence carried into a later scene.
- Why the scene needs to be shown rather than summarized.

Track at least three costly protagonist choices across the full feature. A quiet or constrained person still makes choices: withholding, refusing, consenting, leaving, concealing, protecting, or surrendering something. Ensure the ending follows from prior decisions even when chance plays a role.

Pressure-test the middle. If a recurring workplace, institution, investigation, project, journey, or family obligation appears, give it an evolving problem with consequences. It must do more than reflect the theme. If a central antagonist disappears for a long interval, track how that pressure remains active or deliberately changes.

For nonlinear stories, maintain a factual chronology alongside screen order. Each time shift must change our understanding or the present conflict. Keep orientation legible without explaining every transition.

Choose several potential anchor scenes distributed across the film: an opening that establishes the particular movie, an encounter that changes a relationship, a public pressure scene, a private contradiction, a late irreversible choice, and an ending image or action. These are functions, not a mandate to use six set pieces or a standard formula.

## 4. Draft the complete screenplay

Write scenes in sequence, act by act, into actual files. Deliver complete scenes with action and dialogue. Never substitute treatment prose, omitted dialogue, “continue similarly,” or an outline for pages of screenplay. Keep a progress file if the task spans sessions so the next session resumes from the exact unfinished unit.

Action must describe something that can be photographed, heard, performed, or clearly communicated through film. Prefer precise behavior and physical consequence to explaining what a character symbolizes. Keep action paragraphs readable. Use interior interpretation sparingly and support it with playable behavior.

Dialogue should have tactics, resistance, evasion, misunderstanding, and changing status. Characters should not all speak with the writer's insight. Vary rhythms and vocabulary according to personality and situation. Let people be practical, petty, funny, distracted, mistaken, or embarrassed when that serves the scene.

Build tonal variation appropriate to genre. Relief, pleasure, competence, absurdity, warmth, or sensual detail can make pressure more powerful. Relentless solemnity is not depth. Do not force every scene to have an elegant final line or every image to become a symbol.

Motifs should change meaning as the story develops. A repeated corridor, object, gesture, sound, or phrase must gain pressure, reversal, or consequence. Cut ornamental echoes. Use silence and withheld information deliberately; neither should conceal the absence of a dramatic event.

Historical or source-based work needs a research ledger. Separate documented events, disputed accounts, composites, invented dialogue, and deliberate chronology changes. Verify important claims from credible sources when research tools are available. Record links and what each source supports. If verification is unavailable, mark the claim unresolved. Do not turn creative plausibility into a claim of historical fact. Check the rights status of source editions and translations before reproducing passages.

## 5. Perform structural review before line editing

Read the entire draft as a skeptical story editor. Write `development/review.md` with concrete scene evidence, the five most consequential problems, what must be protected, and an ordered revision plan. A review is useful only if it can identify weaknesses in the writing just produced.

Answer these questions honestly:

- Can we state the pursuit we are following through the whole movie?
- Does each major section advance, complicate, or defeat that pursuit?
- Where does the protagonist cause the next problem?
- Do the opening and ending fulfill the same dramatic promise?
- Does the title earn its place in the back half?
- Does the middle escalate rather than collect variations of the premise?
- Are important relationships structurally distinct?
- Do supporting characters make consequential choices?
- Are chronology and transitions understandable on a first viewing?
- Does the final choice cost something we have learned to value?
- Where is atmosphere standing in for an event?
- Which scenes can be removed without changing anything downstream?

Implement the important repairs. Rebuild weak sequences rather than protecting attractive sentences. Re-read neighboring scenes and downstream consequences after a structural change. Update the outline and scene map to describe the actual draft.

Then do separate passes for character voices, dialogue, action specificity, pacing, tonal variation, repetition, and production scope. Replace summary with playable beats where an important event is being skipped. Compress passages where multiple beats do the same work.

Use bounded, evidence-based revision cycles. Each cycle should record a problem, affected scenes, an intervention, and the result in `development/revision_log.md`. Stop when additional edits become cosmetic churn or introduce regressions. A high count of edits is not evidence of a strong screenplay.

## 6. Derive a development package from the finished draft

For full-package scope, write the following modules in `package/`. Adapt the emphasis to the genre and financing ambition:

1. Logline, short synopsis, and full synopsis with the actual ending.
2. A complete prose treatment following the actual screenplay.
3. Character breakdowns describing behavior, conflict, and arcs.
4. Tone, visual world, sound, point of view, and formal rules.
5. Comparable films and positioning: what each comparison helps explain and where it differs.
6. Casting rationale and performance opportunities, with targets labeled as proposals.
7. Director targets grouped by aspiration and plausible fit, with reasons.
8. Producer or company targets with reasons and verification status.
9. Awards strategy if appropriate to the film and resources.
10. Festival or alternative launch strategy suited to the intended audience.
11. Budget and production scope, assumptions, cost drivers, and controllable variables.
12. Scene showcase drawn from existing scenes and stable scene IDs.
13. Marketing description and audience hook.
14. Several distinct taglines consistent with the actual movie.
15. Appendix covering risks, mitigations, research/rights issues, and packaging next steps.

Do not let the package describe the stronger film you wish you had written. If a claim depends on a nonexistent scene, revise the script deliberately or remove the claim. Update all documents after moving characters, changing the ending, or revising the production plan.

Keep financial numbers explicitly preliminary unless supported by a real budget. Distinguish a comparable film's artistic relevance from evidence of commercial performance. Verify current roles, credits, eligibility rules, incentives, market figures, and availability when making factual claims. A proposed target is not attached, interested, contacted, or available. Festival selection, distribution, awards, and revenue are possibilities, never promised outcomes.

## 7. Write pitches for distinct readers

For full-package scope, create the general pitch and these fifteen stakeholder pitches under `one_pagers/`. Each must fit one actual compiled page at readable typography. Prioritize relevant information rather than shrinking the font to rescue excess copy.

- General: premise, emotional hook, audience, form, production profile.
- Actor: character contradictions, arc, playable scenes, why the role fits.
- Director: formal opportunity, perspective, relationships, cinematic problems worth solving.
- Financier: scope, financing assumptions, audience, risks, packaging dependencies.
- Producer: practical development needs and the route to assembling the project.
- Distributor: audience promise, positioning, release considerations, differentiators.
- Streamer: platform audience fit and why the film can sustain attention.
- Festival: artistic identity and the specific programming fit, without claiming selection.
- Awards: demonstrable craft and performance strengths with a realistic campaign premise.
- Co-production: locations, creative contributions, likely partners, unresolved qualification issues.
- Public funder: cultural value, access, relevant eligibility questions, proposed public benefit.
- Talent representative: career fit, scope of role, package status, and a clear proposed next step.
- Exhibitor: theatrical experience, audience, and programming proposition.
- Cultural partner: relevance, possible programming, and a concrete mutual benefit.
- Press: a truthful angle and film description without invented reviews or endorsements.
- Craft department: visual, sound, design, costume, or editorial opportunities grounded in scenes.

These are draft materials. Do not send outreach, imply endorsement, or invent contact details. If a pitch type is inappropriate, explain the mismatch and adapt its content rather than fabricate a business case.

## 8. Maintain a working publishing repository

If this project includes the supplied scaffold, reuse its Makefile, fonts, shared macros, and document entry points. Otherwise create equivalent modular LaTeX infrastructure supporting Tectonic or latexmk with XeLaTeX.

Keep shared metadata in `common/metadata.tex`: title, uppercase title, subtitle, author/credit, year, date, draft, logline, genre, rating assumption, lead target/status, preliminary budget range, and runtime estimate. Make PDF metadata, title pages, headers, and pitches agree. Do not place a named actor in a “starring” credit without an actual attachment.

Use screenplay layout rather than an article styled to resemble a script: approximately 12-point monospaced type, readable scene headings and action, proper cue/dialogue indents, page numbers, and reliable page breaks. The supplied scaffold uses these macros:

```tex
\scene{INT. LOCATION -- NIGHT}
\action{A visible action changes the situation.}
\character{CHARACTER NAME}
\paren{only when necessary}
\dialogue{Performable dialogue.}
\transition{CUT TO:}
\titlecard{A PLACE OR DATE, IF NEEDED}
```

The scaffold has six act files for convenience. Change the entry point and files when this story needs a different structure. Use movement title pages only as a considered formal choice; distinguish their pages from dramatic pages when reporting length.

Use a separate, restrained design for development materials. Preserve font licenses. Escape LaTeX special characters in prose and metadata, keep relative paths portable, and avoid machine-specific font paths. Keep source editable and avoid unnecessary dependencies.

## 9. Verify the deliverables

Record the selected screenplay, package sections and pitches in development/package_options.json. Run `python3 scripts/story_check.py build` to compile only the selected outputs; `make all` is for every template. Resolve compilation errors. Investigate overfull boxes, orphaned cues/headings, duplicate page anchors, and overflow. Confirm every expected PDF exists and has a plausible page count. Verify every one-pager is exactly one page.

Inspect rendered samples of the screenplay opening, dialogue-heavy pages, act boundaries, package contents, and each pitch. Repair layout issues without distorting typography to hit a page target. If rendering tools are unavailable, state that visual verification remains outstanding.

Search for stale titles, old character names, copied setting details, obsolete movement names, contradictory dates, unearned attachment claims, and all DRAFT PLACEHOLDER text. Check pitch and treatment claims against the final scene map. Report actual page counts, including how title and divider pages affect the number.

Maintain `development/continuity.md` for names, ages, chronology, relationships, locations, props, knowledge states, recurring problems, and ending consequences. Maintain `development/status.md` with completed files, known limitations, unresolved research, last verification, and the exact next action if work remains. Never label a scaffold or an incomplete draft as a finished film package.

## 10. Deliver a usable handoff

Update the README with the real title, logline, file map, prerequisites, build commands, actual output inventory, and honest status. Keep private development criticism separate from outward-facing package copy.

In your final response, link the screenplay, development package, pitches, and source. State what was drafted, what was revised, what was compiled and visually checked, and what remains unresolved. Separate a generated creative draft from professional legal, historical, financial, or production validation.

Start by reading the brief and repository, write the plan, and begin the work. The goal is a specific, emotionally persuasive, producible story with coherent supporting materials and a repeatable build.

## Installed commands, research, and quality controls

The installed suite exposes the same craft guidance in Claude Code (/story…) and Codex ($story… or the skill picker). Use the local skill procedure instead of pretending a shell tracker generates a screenplay. The writer's requested deliverable and format take precedence over the default full feature package. Diagnose imported drafts before starting new-project discovery.

Record original, based-on, or inspired-by in research/source_mode.json. Based-on work needs fidelity to central documented events; inspired-by permits a looser premise while clearly identifying invented people, scenes, dialogue, composites and changed chronology. Use story-research for bounded chronology, relationships and context passes, then reconcile findings into research/claims.json with inspected source locations, evidence states and contradictions. Keep one coordinating author responsible for creative decisions. Never describe invented content as verified fact or claim rights/legal clearance from a ledger. Audit the proposed truth label against the actual screenplay and package with story-truth before final handoff.

Use story-bechdel and story-quality as separate evidence-based checks. Confirm character identities rather than inferring gender from names. A named-women Bechdel assessment reports PASS/FAIL/UNCLEAR and scope, with a specific conversation and subject. A pass does not establish strong characterization or a good film. Review agency, causality, escalation, voices, supporting-character independence, emotional range, ending, title payoff and production scope with stable findings and scene evidence. Store reports against the current draft fingerprint, rerun after revisions, and require a pass only if the writer chose that Bechdel target. No test should be manipulated with a token scene.

Optional helper teams follow TEAMS.md and development/teams.json. Default mode is off: perform research and review sequentially. Only enable bounded native workers when the writer chooses ask/auto or explicitly requests delegation, and the current host actually supports it. Check plan/tool limits, keep one author, prohibit nested teams/new paid services, and record actual assignments and limitations. Keep these controls in Advanced; ordinary writers need only one conversation.

## Adapted screenplays and the default quality standard

A supplied novel, memoir, article, play, short story, nonfiction work or transcript may be the starting material. Use story-import to preserve/extract it and story-adapt with ADAPTATION.md to read the selected scope, establish the fidelity contract, transform interiority into cinematic behavior, track compression/omissions/invention and map source locations to actual scenes. A fictional adaptation can use original factual mode; a memoir may require based-on or inspired-by research. Public-domain or permission assertions are recorded with their basis, never treated as automatic legal clearance. Preserve the original and writer-approved boundaries.

Beginner and expert runs receive the same default quality process in DELIVERY.md: full-draft diagnosis, consequential repairs, continuity/agency/tone/source checks, package alignment and actual all-page PDF inspection. The writer should not need specialist vocabulary to request this work. Use bounded, targeted repair/review instead of repetitive whole-project calls. Final delivery uses scripts/delivery.py and current editorial, factual/adaptation, build and visual receipts. No automatic test guarantees artistic success.
