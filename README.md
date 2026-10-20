# Story Factory

**Your idea. Your voice. A writing room that carries the work forward.**

Story Factory helps you and your AI assistant develop an idea into a screenplay, revise what is weak, and prepare the materials you want to share. Start with a sentence, a finished script, or a book you want to adapt. You stay the author. Your creative decisions govern.

**[Visit the step-by-step website](https://jayzalowitz.github.io/story-factory/)** · **[Download Story Factory](https://github.com/jayzalowitz/story-factory/releases/download/v0.2.0-preview.3/story-factory-0.2.0-preview.3.zip)** · **[Read a finished screenplay](https://jayzalowitz.github.io/story-factory/examples/the-letter-to-the-father/screenplay.pdf)** · [View on GitHub](https://github.com/jayzalowitz/story-factory)

No coding experience required. New to AI writing assistants? [Start with the beginner guide](docs/START_HERE.md).

## One command, the whole process

**`/story-run` in Claude Code · `$story-run` in Codex**

After the short setup below, this is the only writing command you need. Add your idea and let the assistant coordinate the work:

**Explore → research when needed → characters and outline → screenplay → review and revision → selected materials → inspected PDFs.**

For the full kind of project shown by *The Letter to the Father*, paste:

> /story-run My idea is: [your idea]. Create a separate feature-film project and carry it from discovery and research where needed through characters, outline, complete screenplay, full-draft review, meaningful revisions, continuity and Bechdel checks, all 15 studio-package sections, all 16 pitches, and built, visually inspected PDFs with editable sources. Ask me one useful question at a time for important creative choices; handle the routine steps and save progress between sessions. Do not send or publish my work.

**Codex:** replace `/story-run` with `$story-run`. Ask for dry wit and restrained writing if you want those qualities from the example. The full selection produces **18 PDFs**: screenplay, assembled studio package, and sixteen pitches. You can request fewer materials in the same command.

One command coordinates the process; you still make creative choices. A feature can span several sessions or usage resets. Reopen your story folder and use `/story-resume` (Claude) or `$story-resume` (Codex) to continue. Missing tools and unfinished checks stay visible. *The Letter to the Father* predates these commands: this is its extracted workflow, not a promise of identical writing or page counts.

## A draft gets challenged, not just generated

**Write → read the whole draft → find the consequential flaws → revise → recheck → package and inspect.** The assistant carries the loop and preserves your decisions. Reviews cite actual scenes and check character agency, continuity, relevant source fidelity and ending payoff. The **Bechdel assessment** asks whether two named women converse about something other than a man. It reports PASS, FAIL or UNCLEAR honestly; passing is required only if you choose that goal. A pass does not establish character depth or artistic quality. Revision rounds focus on consequential repairs and stop with remaining concerns recorded, rather than running endlessly.

**Why a project folder matters:** even a leading AI model can consider only a limited amount of material at once. The screenplay, research, old drafts and conversation can grow beyond that space, even while the chat still appears on your screen. Story Factory saves the manuscript, story bible, sources, review findings and next action in files. The assistant reads what each stage needs, saves checkpoints and reloads relevant records across sessions. Full-draft reviews still cover the entire current draft, in tracked sections when needed. This makes progress recoverable; it does not give an AI unlimited memory. [How context and quality work](docs/CONTEXT_AND_QUALITY.md).

## Your first session

1. Choose a writing assistant that can work with files: **Claude Code** or **Codex**. The website explains accounts, plans, apps, and opening a project folder. You only need one. Story Factory is free; your chosen AI service has its own usage limits and possible charges.
2. [Download this project](https://github.com/jayzalowitz/story-factory/releases/download/v0.2.0-preview.3/story-factory-0.2.0-preview.3.zip) and unzip it. Open the resulting folder in your assistant.
3. Paste this message:

> Set up Story Factory for my current assistant in this folder using its install.py. I am new to this: explain anything I must do in plain language. Check Python is available first. Install the project skills for my current assistant, then tell me how to reopen this folder if needed. Help me create a separate story project without overwriting anything. My starting idea is: [your idea]. Ask one useful question at a time. I will choose which final files I want. Do not publish or send my work.

Once the commands appear, use **`/story-run` in Claude Code** or **`$story-run` in Codex** with the example above. Use `story` if you only want help choosing a next step. These are messages to your assistant, not commands you need to type into a computer terminal. Codex also offers a skill picker (`/skills`).

Starting with a novel, memoir, article, play or other source? Use `/story-adapt` (Claude) or `$story-adapt` (Codex). It helps read the material, agree what to preserve or change, turn it into scenes, and track departures. Use `story-import` to preserve and extract the original. [Adaptation guide](docs/ADAPTATION.md).

Already have a script? Ask `/story-studio` (Claude) or `$story-studio` (Codex) to read it, explain the strongest improvements, and let you choose what to change. It preserves your original and records your decisions.

## Choose what you want to make

You can stop at an idea, outline, draft, or revision. Every final document is optional: a screenplay; any of the 15 development-package sections; and any of 16 reader-specific pitches. For example:

> I only need a screenplay, a synopsis, character descriptions, and an actor pitch. Leave out budgets, awards, and the other pitches.

The assistant records your choices and builds only those PDFs. A full selection produces 18 PDFs: a screenplay, one assembled studio package, and 16 pitches. See [all the choices](docs/PACKAGE.md).

You do not need to manage the reviews. The assistant reads the full draft, identifies consequential weaknesses, revises, checks continuity and character agency, and keeps the package faithful to the screenplay. It also records a Bechdel assessment using actual scenes and inspects every final PDF page. A passing test or an attractive document does not guarantee a great film. Your story chooses the tone; the example’s dry wit and restraint are available choices.

## Real stories and real choices

Choose original fiction, based on a true story, or inspired by true events. The source-based paths add research, a record of claims and sources, clear distinctions between facts and invented scenes, and a final audit against the script. They do not provide legal clearance or permission to use someone else's material.

Most people can stay in one conversation. Optional helper teams for research and review are tucked into [Advanced settings](docs/ADVANCED.md); they are off by default and never require a second subscription or a new API service.

## See what finished work looks like

<a href="https://jayzalowitz.github.io/story-factory/examples/the-ledger-room/screenplay.pdf"><img src="site/assets/ledger-room-screenplay.png" width="220" alt="Opening scene from the new Ledger Room screenplay"></a> <a href="https://jayzalowitz.github.io/story-factory/examples/the-ledger-room/studio-package.pdf"><img src="site/assets/ledger-room-package.png" width="220" alt="Cover of its complete studio package"></a>

*Actual pages from the new feature demonstration. Select either page to open its PDF.*

[The Letter to the Father](examples/the-letter-to-the-father/README.md) is the feature project from which this process was extracted: a measured [106-page screenplay](site/examples/the-letter-to-the-father/screenplay.pdf), [45-page studio package](site/examples/the-letter-to-the-father/studio-package.pdf), and 16 pitches. [Browse the example gallery](https://jayzalowitz.github.io/story-factory/#examples) to read the public PDFs. Its original brief and development critique are preserved as historical guidance. These are development examples; proposed casting, budgets, financing and awards language are illustrative. They are not confirmed attachments, research certification, or sales claims.

The feature predates these commands. It shows the class of output the toolkit is designed to support, rather than proving one command recreates that quality. [The Night Window](examples/the-night-window/README.md) is a newly written short demonstration with a 10-page screenplay, a 17-page package, and sixteen one-page pitches, produced and checked on this agent host. New examples and [worked sessions](examples/WALKTHROUGH.md) show how to use the system.

[The Ledger Room](examples/the-ledger-room/README.md) is a newly created full feature with an independent AI read, substantive revision and a complete optional package. [Twelve Seconds](examples/adaptation/README.md) and [The Pool](examples/true-story/inspired-by/README.md) show adaptation and inspired-by research promises. Review records explain what was checked and what remains uncertain.

## Prefer an ordinary chat?

Use the [full writing prompt](MASTER_PROMPT.md) or [short writing guide](WRITING_GUIDE.md) in ChatGPT, Claude, Grok, or another chat assistant. You can develop the story that way. The installed commands, saved progress, helper teams, and verified PDF production require a compatible assistant with file/tool access. We do not claim a native Grok integration.

[Beginner setup](docs/START_HERE.md) · [All 21 commands and examples](docs/COMMANDS.md) · [Setup for a helper](docs/SETUP.md) · [Full process](WORKFLOW.md) · [Where this began](docs/ORIGIN.md)

The working pattern is inspired by [Garry Tan's gstack](https://github.com/garrytan/gstack): explore, challenge, build, review, verify, and hand off. This is an independent storytelling toolkit; gstack is not required. Story Factory never contacts talent, submits scripts, or publishes your work merely because you ask it to write.

For maintainers: [compatibility and test evidence](docs/COMPATIBILITY.md) · [full conversation audit](docs/CHAT_GOALS_AUDIT.md) · [next-phase progress](docs/NEXT_PHASE.md).
