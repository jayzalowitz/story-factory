# Upgrade without losing your story

Keep a backup of your story folder. Download the new version into a separate toolkit folder. Your screenplay, source material and decisions stay in the existing story folder.

Ask your assistant:

> Compare this new toolkit with my existing story project. First run the new toolkit's story_factory/upgrade_project.py --project MY_STORY --check. If the helper preflight passes, refresh those helper scripts, then install the new project skills for my chosen assistant. Preserve all manuscripts, decisions, research and local edits. Show me any ownership conflict instead of overwriting it.

The order matters: refresh helper scripts from the new toolkit **before** replacing old installed skills. The old portable toolkit can establish which scripts came from Story Factory. Newly generated projects also have .story-factory-tools.json ownership hashes. Modified/unowned helpers block the entire helper refresh before anything is written. The installer independently preserves changed/unowned skills.

No screenplay, metadata, fonts, layout, story bible, research, fidelity contract or decision log is automatically replaced. If templates changed, ask the assistant to compare and apply only necessary changes after preserving your custom version. Keep the old toolkit/backup until you can open the story, resume and rebuild selected outputs. Reopen the assistant session to discover new commands.

A versioned release ZIP includes RELEASE_MANIFEST.json and a separate SHA-256 file. The archive excludes private imports, generated deliveries, installed snapshots, context and build outputs; reviewed public example PDFs are explicit exceptions. The preview compatibility table describes actual native evidence and remaining limits.

This preview strengthens truth-review currency. Existing factual reviews without the expanded bindings need a fresh review of the current truth promise, departures, research/local evidence and audience wording before a new receipt is recorded. Do not copy old verdicts into new fields merely to clear the gate; preserve the earlier report as history and state what was actually rechecked.
