#!/usr/bin/env python3
"""Export the reusable publishing infrastructure into a new, blank story project."""

import argparse
from datetime import date
from pathlib import Path
import re
import shutil


ROOT = Path(__file__).resolve().parents[1]
FACTORY = Path(__file__).resolve().parent
PLACEHOLDER = "DRAFT PLACEHOLDER -- replace before delivery."
SECTIONS = {
    "logline_synopsis": "Logline and Synopses",
    "treatment": "Treatment",
    "character_breakdowns": "Character Breakdowns",
    "tone_visual_world": "Tone and Visual World",
    "comps_and_positioning": "Comparables and Positioning",
    "casting_notes": "Casting Proposals",
    "director_targets": "Director Targets",
    "producer_targets": "Producer Targets",
    "awards_strategy": "Awards Strategy",
    "festival_strategy": "Festival Strategy",
    "budget_and_scope": "Budget and Production Scope",
    "scene_showcase": "Scene Showcase",
    "marketing_blurb": "Marketing Description",
    "poster_taglines": "Taglines",
    "appendix": "Risks, Research, Rights, and Next Steps",
}
PITCHES = {
    "one_pager": "General Pitch",
    "actor_pitch": "Actor Pitch",
    "director_pitch": "Director Pitch",
    "financier_pitch": "Financier Pitch",
    "producer_pitch": "Producer Pitch",
    "distributor_pitch": "Distributor Pitch",
    "streamer_pitch": "Streamer Pitch",
    "festival_pitch": "Festival Pitch",
    "awards_pitch": "Awards Pitch",
    "coproduction_pitch": "Co-production Pitch",
    "public_funder_pitch": "Public Funder Pitch",
    "talent_rep_pitch": "Talent Representative Pitch",
    "exhibitor_pitch": "Exhibitor Pitch",
    "cultural_partnership_pitch": "Cultural Partnership Pitch",
    "press_pitch": "Press Pitch",
    "craft_pitch": "Craft Department Pitch",
}


def tex_escape(value):
    replacements = {
        "\\": r"\textbackslash{}", "&": r"\&", "%": r"\%", "$": r"\$",
        "#": r"\#", "_": r"\_", "{": r"\{", "}": r"\}",
        "~": r"\textasciitilde{}", "^": r"\textasciicircum{}",
    }
    return "".join(replacements.get(char, char) for char in value)


def neutralize(text):
    # Preserve formatting; remove project-specific identifiers and comments.
    return text.replace("The Letter to the Father", "Story Project").replace(
        "kafka", "project"
    ).replace("KAFKA'S APARTMENT", "LOCATION").replace("Kafka sits at the desk...", "A person acts.").replace(
        "KAFKA", "CHARACTER"
    ).replace("The trial begins...", "A voice speaks.")


def create(destination, title):
    destination.mkdir(parents=True, exist_ok=False)

    def write(name, text):
        path = destination / name
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(text, encoding="utf-8")

    for name in ("Makefile", "latexmkrc", ".gitignore"):
        write(name, neutralize((ROOT / name).read_text()))
    shutil.copytree(ROOT / "fonts", destination / "fonts")
    # The original font README contains a workspace-specific link.
    write("fonts/README.md", (ROOT / "fonts/README.md").read_text().replace(
        "/Users/jayzalowitz/conductor/workspaces/the-letter-to-the-father/colombo/fonts/LICENSE.txt",
        "LICENSE.txt",
    ))
    for source in (ROOT / "common").glob("*.tex"):
        if source.name == "metadata.tex":
            continue
        content = neutralize(source.read_text())
        if source.name == "preamble.tex":
            content = content.replace("pdftitle={Story Project}", r"pdftitle={\filmtitle}")
            content = content.replace("% Hyperref setup", "\\input{../common/metadata}\n\n% Hyperref setup")
            # Load metadata once, before hyperref expands the title.
            content = content.rsplit("\\input{../common/metadata}", 1)[0]
        write("common/" + source.name, content)

    metadata = {
        "filmtitle": title, "filmtitleupper": title.upper(),
        "filmsubtitle": "An Original Screenplay", "filmauthor": "Author to be specified",
        "filmyear": str(date.today().year), "filmdraft": "Scaffold -- not a screenplay draft",
        "filmlogline": PLACEHOLDER, "filmgenre": "To be developed",
        "filmrating": "To be assessed", "filmlead": "Unattached -- creative target to be determined",
        "filmbudgetrange": "Preliminary estimate not yet prepared",
        "filmruntime": "To be measured after drafting",
    }
    write("common/metadata.tex", "\n".join(
        rf"\newcommand{{\{key}}}{{{tex_escape(value)}}}" for key, value in metadata.items()
    ) + "\n" + r"\newcommand{\filmdate}{\today}" + "\n")

    for name in ("main_screenplay.tex", "title_page.tex"):
        content = (ROOT / "screenplay" / name).read_text()
        content = re.sub(r"% Movement [IVX]+: [^\n]+", "% Story movement", content)
        write("screenplay/" + name, content)
    for number in range(1, 7):
        write(f"screenplay/act{number}.tex", rf"\scene{{MOVEMENT {number} -- TO BE WRITTEN}}" +
              "\n\n" + rf"\action{{{PLACEHOLDER}}}" + "\n")
    write("package/studio_package.tex", neutralize((ROOT / "package/studio_package.tex").read_text()))
    for name, heading in SECTIONS.items():
        write(f"package/{name}.tex", rf"\section{{{heading}}}" + "\n\n" + PLACEHOLDER + "\n")
    for name, heading in PITCHES.items():
        write(f"one_pagers/{name}.tex", r"""\documentclass[11pt,letterpaper]{article}
\input{../common/preamble}
\input{../common/typography}
\input{../common/studio_package_macros}
\geometry{margin=0.75in}
\pagestyle{empty}
\begin{document}
\begin{center}
{\Large\bfseries\sffamily \filmtitleupper}\\[6pt]
""" + heading + r"""
\end{center}
\textbf{Project status:} Unwritten; no cast or partners attached.

\textbf{Logline:} \filmlogline

""" + PLACEHOLDER + "\n" + r"\end{document}" + "\n")

    shutil.copyfile(FACTORY / "MASTER_PROMPT.md", destination / "MASTER_PROMPT.md")
    shutil.copyfile(FACTORY / "WORKFLOW.md", destination / "WORKFLOW.md")
    (destination / "scripts").mkdir()
    shutil.copyfile(FACTORY / "workflow.py", destination / "scripts/workflow.py")
    write("CLAUDE.md", "# Project instructions\n\nRead MASTER_PROMPT.md and development/brief.md. "
          "Follow the user's requested scope. The source files are publishing scaffolds, not finished creative work. "
          "Replace all DRAFT PLACEHOLDER text and validate all outputs before claiming completion.\n")
    write("AGENTS.md", "# Project instructions\n\nRead CLAUDE.md, WORKFLOW.md, MASTER_PROMPT.md, and development/brief.md. "
          "Run `python3 scripts/workflow.py status` and execute the next stage. "
          "Follow discovery, premise review, structure review, draft, revision, packaging, verification, and handoff in order. "
          "Use artifact-backed completion receipts; never claim a mechanical check establishes creative quality.\n")
    write("development/brief.md", f"# {title}\n\nSeed idea: TO BE PROVIDED\n\n"
          "Genre and audience: TO BE DEVELOPED\n\nScope: Full feature screenplay and development package\n\n"
          "Cast and partners: No attachments\n\nFill in the project brief from MASTER_PROMPT.md before drafting.\n")
    write("development/status.md", "# Status\n\nPublishing scaffold only. No story has been drafted.\n\n"
          "Next action: complete development/brief.md, then follow MASTER_PROMPT.md.\n")
    write("README.md", f"# {title}\n\n"
          "Your story starts here. This folder gives your AI writing assistant a thoughtful process "
          "for turning an idea into a screenplay and the materials to share it. You stay the author.\n\n"
          "## Begin with a conversation\n\n"
          "Open this folder in an AI assistant that can work with files. Tell it:\n\n"
          "> Help me develop my story with Story Factory. Read the project instructions, "
          "explain choices in plain language, and handle the technical steps for me. "
          "Start by asking one useful question about my idea. Do not rush into writing the whole screenplay.\n\n"
          "Then describe whatever you have: a person, an image, a situation, or a rough plot. "
          "You do not need to know the ending. If you already have writing, share it and ask what to protect.\n\n"
          "## What happens next\n\n"
          "First you explore the idea and choose a direction. Then you develop characters, "
          "shape the outline, and write real scenes. After the full draft, the assistant helps "
          "you find and repair the biggest problems before polishing the dialogue. "
          "When you are ready, it can help prepare a synopsis and pitches for different readers.\n\n"
          "Your assistant can keep track of the process in this folder. Ask it for a short "
          "progress update whenever you need one. Everything here starts as a blank template; "
          "nothing is a finished screenplay yet.\n\n"
          "## The guides\n\n"
          "- WORKFLOW.md explains the writing and review steps.\n"
          "- MASTER_PROMPT.md gives the assistant detailed creative instructions.\n"
          "- development/brief.md is a place to keep your starting idea.\n"
          "- development/status.md records where things stand.\n\n"
          "## Optional: make PDFs\n\n"
          "A coding assistant or helper can set up Tectonic, or latexmk with XeLaTeX, "
          "and run `make all`. This produces a screenplay PDF, a development package, "
          "and 16 pitch documents in output/. The templates can compile before any writing "
          "exists, so a successful build does not mean the story is ready.\n\n"
          "Your AI service may require an account or charge for use. Check facts and rights, "
          "keep copies of your work, and read everything before sharing it. "
          "Proposed actors and partners are ideas, not attachments.\n")
    print(f"Created blank story scaffold: {destination}")
    print("Next: fill development/brief.md and run the instructions in MASTER_PROMPT.md.")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("destination", type=Path, help="New directory; must not already exist")
    parser.add_argument("--title", required=True, help="Working title (plain text)")
    args = parser.parse_args()
    if not args.title.strip() or any(ord(char) < 32 or ord(char) == 127 for char in args.title):
        parser.error("title must be nonempty text without control characters")
    destination = args.destination.expanduser().resolve()
    if destination.exists():
        parser.error(f"destination already exists; refusing to overwrite: {destination}")
    create(destination, args.title.strip())


if __name__ == "__main__":
    main()
