# story-setup — Get this project ready

Help a first-time writer get from a downloaded project to a working conversation in their chosen coding assistant. Read `COMMON.md`. Explain each next action in plain language; do not ask the writer to understand terminals, model APIs, subagents, or billing systems just to begin.

## Check the current situation

Identify the actual host and project folder from observed context. Run the project's `python3 scripts/setup_check.py --project . --json` when available. In the toolkit itself the helper is also at `story_factory/setup_check.py`. If Python cannot run, explain that observation and use the official Python installation instructions; do not pretend the check succeeded. Report only what the check observes. CLI presence, copied skill files, an app window, login, account eligibility, remaining usage, native command activation, and successful PDF generation are separate facts.

Ask which assistant the writer wants only if it is unclear. Claude Code uses `/story`; Codex uses `$story` or its skill picker. These are messages inside the assistant, never shell commands. An ordinary provider web-chat subscription does not establish that a local coding assistant can open this project. Guide the writer to the official product's current account, download, and plan pages already linked in the toolkit's beginner guide. Never select a paid plan, enter payment details, infer a user's subscription, request passwords/API keys, or promise a particular quota. Subscription sign-in and separately billed API access are different routes; do not introduce API billing unless the writer explicitly needs it.

## Resolve the next blocker

Use the project-local installer if needed and authorized by setup: `python3 install.py --project "PROJECT_FOLDER" --host claude` or `--host codex` (or both if requested). Find the installer in the bundled toolkit when it is not in the story project itself. Respect its ownership-conflict errors. Never overwrite a writer's modified skill or silently switch to user-wide installation.

Explain how to open the actual project folder in the chosen assistant, reload/restart if its official discovery behavior requires that, and invoke the entrypoint. Confirm the host reads the project brief or another harmless project file. Save an observed activation result only after that real interaction occurs; a setup report cannot certify its own host activation.

Missing PDF tools do not block writing. The included build uses make and either Tectonic or latexmk with XeLaTeX; pdfinfo verifies the results. The Makefile selects latexmk first when installed, so that path also needs XeLaTeX. pdftotext is separately needed for PDF imports. Offer official installation guidance appropriate to the observed operating system. Before installing anything, establish whether the host supports the action and whether the writer wants it. Do not execute downloaded shell commands blindly. When a usage limit stops work, save the current state and explain the provider's actual message; wait, resume later, or use another supported host with the same project. Do not promise a reset time or silently switch to paid API calls.

## Finish with a small success

Offer the appropriate next step: `story-office-hours` for an idea, `story-import` then `story-studio` for an existing screenplay, or `story-import` in adaptation mode for a book, article, play, or other source. Keep advanced team controls and optional memory integrations out of this beginner flow unless asked or needed. End with what actually works, the next action, and any remaining blocker. Never call the complete setup tested merely because files were installed.
