# From an idea to a writing project

This is an illustrative command walkthrough, not a transcript of a model run or evidence of a completed feature. All story material here is newly invented. Replace the sample with your own idea.

## 1. Start a project

In Claude Code:

```text
/story-new Make a project called The Last Signal in ../the-last-signal. It is original fiction: a retired lighthouse keeper receives letters from ships that disappeared years ago. Her daughter has her own plans. Keep it contained.
```

In Codex, the same skill uses the native skill mention:

```text
$story-new Make a project called The Last Signal in ../the-last-signal. It is original fiction: a retired lighthouse keeper receives letters from ships that disappeared years ago. Her daughter has her own plans. Keep it contained.
```

The assistant creates organized files and installs both hosts' commands. Open the new project in your assistant. The source toolkit is not your screenplay project.

## 2. Find the important choice

```text
/story-office-hours I want tenderness and unease. Ask one question at a time. I'm unsure whether the letters are supernatural.
```

A useful first question might be: “What does Mara want the first letter to let her avoid doing today?” A useful provisional answer: she is using it to postpone selling the lighthouse and letting Nina leave. That is a dramatic choice to explore, not an automatic decision the assistant must impose.

## 3. Challenge the premise and give it shape

```text
/story-premise Compare a literal ghost story and a grounded mystery. Recommend the version that gives both women more difficult choices.
/story-outline Keep five locations. Track what each decision changes. The ending should cost Mara something she values.
```

Possible artifacts: a story bible, alternatives, risks, stable scene IDs, chronology, and a scene ledger. The writer chooses whether a real mystery or ambiguous experience serves the film. No worksheet should silently decide that for them.

## 4. Draft and ask for useful criticism

```text
/story-draft Write the first sequence in actual screenplay form. Protect Nina's independent work goals.
/story-review Find the five most consequential problems. Cite scenes. Tell me what to preserve.
/story-revise Repair the repeated kitchen confrontations before polishing dialogue.
/story-bechdel Check the full draft and show the qualifying conversation, or say what fails or remains unclear.
/story-quality Review agency, causality, voices, pacing, the ending, and production scope. Do not confuse a Bechdel pass with a strong screenplay.
```

See [the quality examples](quality/README.md) for concrete weak/strong exchanges and a review finding. Reports describe the actual draft and are invalidated when the screenplay changes.

## 5. Research a real-story version when needed

```text
/story-new Create a separate project inspired by a documented rescue. Do not use the invented lighthouse example as evidence.
/story-research Establish the event timeline, people, and operating context. Use up to three native research workers and reconcile contradictions. Keep invented scenes separate.
/story-truth Check what the outline and pitch can honestly call “inspired by.” Show the sources and deliberate departures.
```

The [research examples](research/README.md) show the ledger structure. They are synthetic; no source in that fixture is evidence. A based-on story needs stronger fidelity to central events than merely borrowing an initial situation. Neither label substitutes for fact checking or establishes rights clearance.

## 6. Prepare only what you need

```text
/story-package Build the full development package and reader-specific pitches from the revised draft.
/story-check Compile the actual PDFs, measure the pages, inspect the layout, and report limitations.
/story-handoff Give me the editable sources, final PDFs, a short status, and any unresolved questions. Do not send them to anyone.
```

For a recipient who requests only a one-page synopsis, ask for that instead. Do not append the default full package. The included print system is designed for feature screenplay packages; a short or a custom submission should use the requested scope.

## Existing draft, shorter path

```text
/story-review Read my existing draft first. Reconstruct the premise and scene logic from what is there. Do not restart discovery or rewrite it yet.
/story-revise Keep the ending, fix the weak middle, and show the consequences of each repair.
```

## Pick up tomorrow, or run the whole process

```text
/story-resume Remind me what we decided and continue the next unfinished sequence.
/story-run Take this project through the full writing process. Make routine decisions, but ask before changing my ending or publishing anything.
```

For Codex, replace each leading slash with `$`: `$story-review`, `$story-run`, and so on. These commands are typed into the coding assistant, not Terminal and not an ordinary chat app that has not installed the skills. Claude and Codex account costs and tool permissions still apply.
