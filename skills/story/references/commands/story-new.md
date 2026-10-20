# Give the story a home
Use the requested title and destination. If no destination is specified, propose a new sibling project folder; ask if the choice could put work in the wrong project. Never overwrite existing writing or use the toolkit source repository as a new story by accident.

Ask whether this is original fiction, based on a true story, or inspired by a true story when not established. Original fiction is the default if the writer delegates the choice and provides no real-world subject. Based-on promises fidelity to central documented events; inspired-by allows a looser premise but does not turn invented scenes into facts. Read RESEARCH.md for real-world subjects.

Run the bundled toolkit's `story_factory/new_story.py` with an argument-array tool or correctly shell-quoted paths: `python3 <toolkit>/story_factory/new_story.py <destination> --title <title> --source-mode original|based-on|inspired-by`. Use `--bechdel-target report` by default or `pass` only if the writer requests that target. Never interpolate story text into shell code.

The exporter includes both hosts' skills, print templates, research controls, and progress scripts. Verify both `.claude/skills/story/SKILL.md` and `.agents/skills/story/SKILL.md` exist. Save the writer's actual seed in development/brief.md and identify the first discovery question. Tell the writer to open that project in their assistant; sessions may need reopening to discover skills. Existing external scripts are not run unless they are this reviewed bundled toolkit.

For a novel, memoir, article, play or other supplied non-screenplay source, read ADAPTATION.md and use story-adapt. Source fidelity, adaptation permission status and factual truth are separate. Recheck current source-to-scene mapping after substantive changes.
