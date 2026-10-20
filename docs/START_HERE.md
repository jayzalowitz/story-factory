# Your first Story Factory project

**Bring an idea. Let the assistant help with setup. Start the writing with one command.**

[Illustrated website](https://jayzalowitz.github.io/story-factory/) · [See finished examples](https://jayzalowitz.github.io/story-factory/#examples) · [Back to the README](../README.md)

You do not need to learn programming. You need an AI assistant that can read and save a folder on your computer. A normal chatbot is enough for discussing ideas; the file-based assistant also organizes the screenplay and makes PDFs.

## 1. Choose one assistant

**Claude:** follow the [official Claude Code desktop guide](https://code.claude.com/docs/en/desktop). Create or sign into a Claude account, check the current plan includes the Code feature you intend to use, download the official desktop app, and select its Code tab. The ordinary Chat tab does not install project commands.

**Codex:** follow the [official quickstart](https://developers.openai.com/codex/quickstart). Sign in with your ChatGPT account using a supported local app or editor setup. Check current availability and usage limits in the [official plan guide](https://developers.openai.com/codex/pricing). You do not need to buy API credits for Story Factory's scripts; separate API billing is relevant only if you deliberately choose that route.

Choose whichever you already use or feel comfortable with. You only need one. Provider plans, apps and limits change: use their current official pages before paying. Story Factory does not sell an AI subscription, ask for your password, or provide unlimited usage. If an employer manages your account, ask whether local project access and research are allowed.

**Grok or another ordinary chat:** you can use the full writing prompt manually. See [official Grok help](https://help.x.com/en/using-x/about-grok) for its access options. We have not validated a native Grok command installer or file-export workflow. Do not purchase a subscription expecting those features here.

## 2. Download and open the project

Use the versioned [download](https://github.com/jayzalowitz/story-factory/releases/download/v0.2.0-preview.3/story-factory-0.2.0-preview.3.zip). Unzip it in a place you can find, such as Documents. GitHub is the place the project files are stored; you do not need a GitHub account to download this public project.

Open your assistant and choose the unzipped folder as its project folder. That gives it the files it needs. Keep your future screenplay in a separate folder; the assistant will create it. Downloading this public toolkit does not make your private screenplay public.

## 3. Let the assistant do setup

Paste:

> Read this project's README and install.py. Check Python is available, then install Story Factory's project skills for this assistant. Explain any action I must take in plain language. Do not change global settings. If commands need a new session, tell me exactly which folder to reopen. Then help create my separate story project. Never overwrite my existing files.

The setup uses Python, a common small program already on many computers. If missing, your assistant should help you obtain it from [python.org](https://www.python.org/downloads/). Do not paste passwords or payment information into the conversation. The installer stays inside the chosen project by default.

If the app asks to approve reading files or running the local installer, approve reading and saving in this chosen folder and running its included installer. The assistant should explain system-tool installation separately. If a command is missing afterward, reopen the session in the same folder and ask the assistant to check the installation. In Codex, also try the skill picker (`/skills`).

## 4. Start the whole process with one command

Copy this into your assistant. Replace `[your idea]` with a sentence or paragraph about the movie you want to make:

> /story-run My idea is [your idea]. Create a separate feature-film project. Carry it from discovery and research where needed through characters, outline, a complete screenplay, full-draft review and revisions, continuity and Bechdel checks, all 15 studio-package sections, all 16 pitches, and built, visually inspected PDFs with editable sources. Ask me one useful question at a time about important creative choices. Handle the routine steps and save progress. Do not send or publish my work.

**Using Codex? Replace `/story-run` with `$story-run`.** These are messages to your assistant, not commands for a terminal window.

This requests the full kind of package shown by *The Letter to the Father*: 18 PDFs—one screenplay, one assembled studio package, and sixteen one-page pitches. You can instead say “only the screenplay and synopsis.” [Every studio component and pitch is optional](PACKAGE.md). You do not need to run `story-new`, `story-office-hours`, or each review command yourself; `story-run` coordinates them.

Say whether the story is invented, based on a true story, or inspired by something real. If you have a novel, memoir, article, play or existing screenplay, say so in the same request and identify the file. The assistant routes preservation, adaptation or studio review as needed. It must read the material before proposing changes, and ask before major rewrites you have not approved.

## 5. Make choices while the assistant carries the work

Answer the questions, choose a direction, and ask for unfamiliar terms in plain language. The assistant develops characters, outline and actual scenes, reviews the complete draft, repairs weaknesses, aligns the selected materials, and checks the final PDFs. Important decisions remain yours.

A full feature takes sustained work and may span several sessions or usage resets. One command coordinates the whole process; it does not remove decisions, tool requirements or usage limits. If interrupted, reopen the story folder and use `/story-resume` in Claude Code or `$story-resume` in Codex. Do not restart from scratch.

## 6. Make, inspect and receive your files

`story-run` includes the final checks and handoff; you do not need extra commands. You can use `story-check` separately whenever you want to check a build. The assistant checks the sources and builds your selected PDFs. PDF creation needs a local typesetting tool (Tectonic, or XeLaTeX with latexmk) and `pdfinfo`; ask the assistant to check these and explain installation if missing. Installing system tools is a separate action you should understand. Writing can continue before print tools are ready.

Have it inspect dialogue pages, page breaks, the package, and every selected pitch. A pitch must fit one readable page. The included `story-handoff` stage collects editable sources, PDFs, actual page counts, known limitations, and a clear next step. Open the PDFs yourself before sending them.

To return later, reopen the **story's folder** and use `/story-resume` (Claude) or `$story-resume` (Codex). Keep a backup of the folder. If usage runs out, ask the assistant to save your current decisions and next action; resume after your allowance resets. No need to understand advanced helper teams to do any of this.

The assistant owns the quality work: full-draft critique, meaningful repairs, continuity/source checks, aligned selected materials and actual PDF inspection. You make creative choices; you do not need to manage a review pipeline. If setup is unclear, use `story-setup`.
