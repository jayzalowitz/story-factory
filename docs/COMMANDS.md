# Writing commands

In Claude Code type `/name`; in Codex type `$name` or choose it with `/skills`. These are assistant messages, never terminal commands. Add your request after the name. Start with `story` if unsure.

| Command | What it does |
|---|---|
| `story` | Choose the next Story Factory command for a story project or explain the command suite. |
| `story-setup` | Check setup and explain missing requirements. |
| `story-import` | Preserve and extract existing writing and source documents. |
| `story-adapt` | Adapt a novel, memoir, article, play or other source into cinematic scenes. |
| `story-new` | Create a fresh film-writing project with templates and skills for Claude Code and Codex. |
| `story-office-hours` | Explore a story seed through a focused conversation before outlining or drafting. |
| `story-research` | Research a based-on or inspired-by true story using source-led native subagent work. |
| `story-premise` | Challenge a film premise, choose its scope, and establish the dramatic promise. |
| `story-outline` | Design characters, causal scenes, chronology, and the structure of a film story. |
| `story-draft` | Write complete screenplay scenes from an established story plan. |
| `story-review` | Diagnose a full screenplay with concrete scene evidence before revising it. |
| `story-studio` | Review an existing screenplay as a studio development editor and ask the writer to choose concrete improvements. |
| `story-revise` | Implement prioritized screenplay repairs and recheck the revised draft. |
| `story-bechdel` | Assess screenplay conversations against a named-women Bechdel test with scene evidence. |
| `story-quality` | Review screenplay craft, representation, and production feasibility with scene evidence. |
| `story-truth` | Audit factual claims, dramatizations, and source-based labels against a research ledger. |
| `story-package` | Create a coherent studio development package and reader-specific pitches from a draft. |
| `story-check` | Compile screenplay deliverables and check actual PDFs, continuity, and completeness. |
| `story-handoff` | Prepare an honest inventory of a story project and its editable deliverables. |
| `story-resume` | Recover story decisions, progress, and the next action from a saved project. |
| `story-run` | Carry a story project through the staged writing and review process within user scope. |

## Examples

```text
/story-new A contained family drama called The Last Ferry. Create a separate project.
/story-office-hours I have an image of two sisters clearing out a projection booth. Find the story with me.
/story-studio Read my existing screenplay. Protect the ending and dry tone. Ask me which major changes to accept.
/story-research Based on a real factory closure. Separate records, family recollections and invented scenes.
/story-package Only a synopsis, character breakdowns and a producer pitch. No awards or financing claims.
/story-check Build only my selected files and inspect the actual PDFs.
/story-resume Tell me where we stopped and continue the next agreed step.
```

Codex equivalents start with `$`, such as `$story-studio Read my existing screenplay…`. `story-run` coordinates the stages; individual commands let you work on one problem. Research/review helpers are optional, off by default. See the [complete walkthrough](../examples/WALKTHROUGH.md), [studio decision session](../examples/STUDIO_SESSION.md), [quality examples](../examples/quality/README.md), and [advanced controls](ADVANCED.md).

Adaptation example: `/story-adapt Adapt my novella into a contained feature. Preserve the ending and dry humor; ask before combining characters.` In Codex, use `$story-adapt`. See [adaptation](ADAPTATION.md). Quality checks are automatic in a full run; beginners need not know every command.
