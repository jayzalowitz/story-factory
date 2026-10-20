# Your first Story Factory project

You do not need to learn programming. You need an AI assistant that can read and save a folder on your computer. A normal chatbot is enough for discussing ideas; the file-based assistant also organizes the screenplay and makes PDFs.

## 1. Choose one assistant

**Claude:** follow the [official Claude Code desktop guide](https://code.claude.com/docs/en/desktop). Create or sign into a Claude account, check the current plan includes the Code feature you intend to use, download the official desktop app, and select its Code tab. The ordinary Chat tab does not install project commands.

**Codex:** follow the [official quickstart](https://developers.openai.com/codex/quickstart). Sign in with your ChatGPT account using a supported local app or editor setup. Check current availability and usage limits in the [official plan guide](https://developers.openai.com/codex/pricing). You do not need to buy API credits for Story Factory's scripts; separate API billing is relevant only if you deliberately choose that route.

Choose whichever you already use or feel comfortable with. You only need one. Provider plans, apps and limits change: use their current official pages before paying. Story Factory does not sell an AI subscription, ask for your password, or provide unlimited usage. If an employer manages your account, ask whether local project access and research are allowed.

**Grok or another ordinary chat:** you can use the full writing prompt manually. See [official Grok help](https://help.x.com/en/using-x/about-grok) for its access options. We have not validated a native Grok command installer or file-export workflow. Do not purchase a subscription expecting those features here.

## 2. Download and open the project

Open [Story Factory on GitHub](https://github.com/jayzalowitz/story-factory), choose the green **Code** button, then **Download ZIP**. Or use the direct [download](https://github.com/jayzalowitz/story-factory/archive/refs/heads/main.zip). Unzip it in a place you can find, such as Documents. GitHub is the place the project files are stored; you do not need a GitHub account to download this public project.

Open your assistant and choose the unzipped folder as its project folder. That gives it the files it needs. Keep your future screenplay in a separate folder; the assistant will create it. Downloading this public toolkit does not make your private screenplay public.

## 3. Let the assistant do setup

Paste:

> Read this project's README and install.py. Check Python is available, then install Story Factory's project skills for this assistant. Explain any action I must take in plain language. Do not change global settings. If commands need a new session, tell me exactly which folder to reopen. Then help create my separate story project. Never overwrite my existing files.

The setup uses Python, a common small program already on many computers. If missing, your assistant should help you obtain it from [python.org](https://www.python.org/downloads/). Do not paste passwords or payment information into the conversation. The installer stays inside the chosen project by default.

If the app asks to approve reading files or running the local installer, inspect the request and approve the intended setup. If a command is missing afterward, reopen the session in the same folder and ask the assistant to check the installation. In Codex, also try the skill picker (`/skills`).

## 4. Start writing

In Claude Code type `/story-new`; in Codex type `$story-new`. Add your idea and a title if you have one. Say whether it is invented, based on a true story, or inspired by something real. The assistant creates a new folder and tells you to open it for the writing sessions.

Then use `/story-office-hours` or `$story-office-hours`. A sentence, a feeling, or a half-formed character is enough. Answer the questions, choose a direction, and ask the assistant to explain any unfamiliar film-development term. Bring an existing screenplay through `story-studio` instead.

## 5. Work through the film

Ask `story-run` to continue through the agreed scope. It develops the premise, characters, outline, actual scenes, review and revisions. You can intervene at any point. Decide which suggestions to accept; studio mode keeps a decision record. For a full feature this takes sustained writing and revision, often across several sessions. It is not a one-click quality guarantee.

Tell the assistant which [materials](PACKAGE.md) you want. You can leave out every pitch and simply make the script. For true-story work, inspect the research and what remains uncertain before accepting factual claims. Read and revise the screenplay before investing in packaging.

## 6. Make, inspect and receive your files

Use `story-check`. The assistant checks the sources and builds your selected PDFs. PDF creation needs a local typesetting tool (Tectonic, or XeLaTeX with latexmk) and `pdfinfo`; ask the assistant to check these and explain installation if missing. Installing system tools is a separate action you should understand. Writing can continue before print tools are ready.

Have it inspect dialogue pages, page breaks, the package, and every selected pitch. A pitch must fit one readable page. Use `story-handoff` for editable sources, PDFs, actual page counts, known limitations, and a clear next step. Open the PDFs yourself before sending them.

To return later, reopen the **story's folder** and use `story-resume`. Keep a backup of the folder. If usage runs out, ask the assistant to save your current decisions and next action; resume after your allowance resets. No need to understand advanced helper teams to do any of this.
