# Story Factory

**Bring an idea or a screenplay. Leave with a stronger story and the materials you choose.**

A writing room for you and your AI assistant: explore the idea, develop characters, build scenes, write the script, question what is weak, revise, and prepare it for other people to read. You stay the author. Your creative decisions govern.

**[Start here: the illustrated, step-by-step website](https://jayzalowitz.github.io/story-factory/)** — including help choosing an AI assistant and getting set up. No coding experience required.

## Your first session

1. Choose a writing assistant that can work with files: **Claude Code** or **Codex**. The website explains accounts, plans, apps, and opening a project folder. You only need one. Story Factory is free; your chosen AI service has its own usage limits and possible charges.
2. [Download this project](https://github.com/jayzalowitz/story-factory/releases/download/v0.2.0-preview.1/story-factory-0.2.0-preview.1.zip) and unzip it. Open the resulting folder in your assistant.
3. Paste this message:

> Set up Story Factory for my current assistant in this folder using its install.py. I am new to this: explain anything I must do in plain language. Check Python is available first. Install the project skills for my current assistant, then tell me how to reopen this folder if needed. Help me create a separate story project without overwriting anything. My starting idea is: [your idea]. Ask one useful question at a time. I will choose which final files I want. Do not publish or send my work.

Once the commands appear, type **`/story` in Claude Code** or **`$story` in Codex**. These are messages to your assistant, not commands you need to type into a computer terminal. Codex also offers a skill picker (`/skills`).

Starting with a novel, memoir, article, play or other source? Use `/story-adapt` (Claude) or `$story-adapt` (Codex). It helps read the material, agree what to preserve or change, turn it into scenes, and track departures. Use `story-import` to preserve and extract the original. [Adaptation guide](docs/ADAPTATION.md).

Already have a script? Ask `/story-studio` (Claude) or `$story-studio` (Codex) to read it, explain the strongest improvements, and let you choose what to change. It preserves your original and records your decisions.

## Choose what you want to make

You can stop at an idea, outline, draft, or revision. Every final document is optional: a screenplay; any of the 15 development-package sections; and any of 16 reader-specific pitches. For example:

> I only need a screenplay, a synopsis, character descriptions, and an actor pitch. Leave out budgets, awards, and the other pitches.

The assistant records your choices and builds only those PDFs. A full selection produces 18 PDFs: a screenplay, one assembled studio package, and 16 pitches. See [all the choices](docs/PACKAGE.md).

The assistant carries the quality process even for a beginner: full-draft diagnosis, substantive repairs, source and continuity checks, aligned materials, and inspection of every final PDF page. You do not need to ask for specialist reviews. The process includes honest story review, continuity, character agency, a scene-evidenced Bechdel assessment, and checks of the actual PDFs. A passing test or an attractive document does not guarantee a great film. Dry wit and restrained writing are available creative choices, not a forced style for every story.

## Real stories and real choices

Choose original fiction, based on a true story, or inspired by true events. The source-based paths add research, a record of claims and sources, clear distinctions between facts and invented scenes, and a final audit against the script. They do not provide legal clearance or permission to use someone else's material.

Most people can stay in one conversation. Optional helper teams for research and review are tucked into [Advanced settings](docs/ADVANCED.md); they are off by default and never require a second subscription or a new API service.

## See what finished work looks like

[The Letter to the Father](examples/the-letter-to-the-father/README.md) is the feature project from which this process was extracted: a measured 106-page screenplay, 45-page studio package, and 16 pitches. Its original brief and development critique are preserved as historical guidance. These are development examples; proposed casting, budgets, financing and awards language are illustrative. They are not confirmed attachments, research certification, or sales claims.

The feature predates these commands. It shows the class of output the toolkit is designed to support, rather than proving one command recreates that quality. [The Night Window](examples/the-night-window/README.md) is a newly written short demonstration with a 10-page screenplay, a 17-page package, and sixteen one-page pitches, produced and checked on this agent host. New examples and [worked sessions](examples/WALKTHROUGH.md) show how to use the system.

[The Ledger Room](examples/the-ledger-room/README.md) is a newly created full feature with an independent AI read, substantive revision and a complete optional package. [Twelve Seconds](examples/adaptation/README.md) and [The Pool](examples/true-story/inspired-by/README.md) show adaptation and inspired-by research promises. Review records explain what was checked and what remains uncertain.

## Prefer an ordinary chat?

Use the [full writing prompt](MASTER_PROMPT.md) or [short writing guide](WRITING_GUIDE.md) in ChatGPT, Claude, Grok, or another chat assistant. You can develop the story that way. The installed commands, saved progress, helper teams, and verified PDF production require a compatible assistant with file/tool access. We do not claim a native Grok integration.

[Beginner setup](docs/START_HERE.md) · [All 21 commands and examples](docs/COMMANDS.md) · [Setup for a helper](docs/SETUP.md) · [Full process](WORKFLOW.md) · [Where this began](docs/ORIGIN.md)

The working pattern is inspired by [Garry Tan's gstack](https://github.com/garrytan/gstack): explore, challenge, build, review, verify, and hand off. This is an independent storytelling toolkit; gstack is not required. Story Factory never contacts talent, submits scripts, or publishes your work merely because you ask it to write.

For maintainers: [compatibility and test evidence](docs/COMPATIBILITY.md) · [next-phase progress](docs/NEXT_PHASE.md).
