# Your writing-room guide
Read the project brief and run `python3 scripts/workflow.py status` if it exists. If no project exists, recommend story-new; if the writer has only an idea, route to story-office-hours. Explain the next useful command in plain language. Do not start an unrequested full feature merely because the router was invoked. For a full run explicitly requested by the writer, use the story-run procedure. Native host support: Claude uses /story-name; Codex uses $story-name or its skill picker. These are agent instructions, not shell commands.

Return the recommended next move, why it matters, and the concrete artifact it will produce. If the writer wants a menu, read COMMANDS.json in the bundled toolkit. Do not run network or publication actions just to list commands.

If setup is unclear, use story-setup. Route supplied files through story-import; route a novel, memoir, article, play or other non-screenplay source through story-adapt. Adaptation is separate from whether the source is factual. Every complete run carries DELIVERY.md quality checks automatically; a beginner need not request specialist reviews.
