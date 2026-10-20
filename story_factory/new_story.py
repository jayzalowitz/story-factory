#!/usr/bin/env python3
"""Export the reusable publishing infrastructure into a new, blank story project."""

import argparse
import json
import subprocess
import sys
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


def create(destination, title, source_mode="original", bechdel_target="report", install_skills=True):
    destination.mkdir(parents=True, exist_ok=False)

    def write(name, text):
        path = destination / name
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(text, encoding="utf-8")

    for name in ("Makefile", "latexmkrc", ".gitignore"):
        write(name, neutralize((ROOT / name).read_text()))
    shutil.copytree(ROOT / "fonts", destination / "fonts")
    for source in (ROOT / "common").glob("*.tex"):
        if source.name == "metadata.tex":
            continue
        content = neutralize(source.read_text())
        if source.name == "preamble.tex":
            # Source templates may already be exported. Normalize, never truncate.
            content = re.sub(r"(?m)^\\input\{\.\./common/metadata\}\s*\n?", "", content)
            content = content.replace("pdftitle={Story Project}", r"pdftitle={\filmtitle}")
            content = content.replace("% Hyperref setup", "\\input{../common/metadata}\n\n% Hyperref setup")
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
    shutil.copyfile(FACTORY / "story_check.py", destination / "scripts/story_check.py")
    shutil.copyfile(FACTORY / "package_options.py", destination / "scripts/package_options.py")
    from_package = {"screenplay": True, "sections": list(SECTIONS), "pitches": list(PITCHES)}
    write("development/package_options.json", json.dumps(from_package, indent=2) + "\n")
    write("CLAUDE.md", "# Project instructions\n\nRead MASTER_PROMPT.md and development/brief.md. "
          "Follow the user's requested scope. The source files are publishing scaffolds, not finished creative work. "
          "Replace all DRAFT PLACEHOLDER text and validate all outputs before claiming completion.\n")
    write("AGENTS.md", "# Project instructions\n\nRead CLAUDE.md, WORKFLOW.md, MASTER_PROMPT.md, and development/brief.md. "
          "Run `python3 scripts/workflow.py status` and execute the next stage. "
          "Follow discovery, premise review, structure review, draft, revision, packaging, verification, and handoff in order. "
          "Use artifact-backed completion receipts; never claim a mechanical check establishes creative quality.\n")
    write("research/source_mode.json", json.dumps({
        "mode": source_mode, "subject": "", "time_range": "", "intended_claim": "To be established with the writer",
        "creative_departures": [], "research_budget": {"max_workers": 3, "max_sources_per_worker": 10}, "living_people": []
    }, indent=2) + "\n")
    write("research/claims.json", json.dumps({"sources": [], "claims": []}, indent=2) + "\n")
    write("development/teams.json", json.dumps({
        "mode": "off", "max_workers": 3, "max_rounds": 1, "max_sources_per_worker": 10,
        "allowed_tasks": ["research", "continuity", "quality", "package-review"],
        "allow_nested": False, "new_paid_services": False
    }, indent=2) + "\n")
    write("development/preferences.json", json.dumps({"bechdel_target": bechdel_target}, indent=2) + "\n")
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
          "## Your writing-room commands\n\n"
          "In Claude Code, start with `/story-office-hours`; in Codex, use `$story-office-hours`. "
          "Use story-outline, story-draft, story-review, and story-revise as you develop the story. "
          "The story-bechdel, story-quality, and story-truth checks provide specific evidence, "
          "not automatic praise. Use story-run for the complete process and story-resume to pick up later. "
          "These commands need the installed skills; a helper can install them if omitted.\n\n"
          "## Optional: make PDFs\n\n"
          "A coding assistant or helper can set up Tectonic, or latexmk with XeLaTeX, "
          "and Poppler for PDF measurement. Tell the assistant which documents you want, then "
          "run `python3 scripts/story_check.py build` to create and measure only those PDFs in output/. "
          "The complete selection is a screenplay, development package and 16 pitches. "
          "The templates can compile before any writing "
          "exists, so a successful build does not mean the story is ready.\n\n"
          "Your AI service may require an account or charge for use. Check facts and rights, "
          "keep copies of your work, and read everything before sharing it. "
          "Proposed actors and partners are ideas, not attachments.\n")
    if install_skills:
        subprocess.run([sys.executable, str(ROOT / "install.py"), "--project", str(destination), "--host", "both"], check=True)
    print(f"Created blank story scaffold: {destination}")
    print("Next: open this folder in your assistant. Claude: /story-office-hours; Codex: $story-office-hours.")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("destination", type=Path, help="New directory; must not already exist")
    parser.add_argument("--title", required=True, help="Working title (plain text)")
    parser.add_argument("--source-mode", choices=["original", "based-on", "inspired-by"], default="original")
    parser.add_argument("--bechdel-target", choices=["report", "pass"], default="report")
    parser.add_argument("--no-skills", action="store_true", help="Export writing/PDF files only, without installing commands")
    args = parser.parse_args()
    if not args.title.strip() or any(ord(char) < 32 or ord(char) == 127 for char in args.title):
        parser.error("title must be nonempty text without control characters")
    destination = args.destination.expanduser().resolve()
    if destination.exists():
        parser.error(f"destination already exists; refusing to overwrite: {destination}")
    create(destination, args.title.strip(), args.source_mode, args.bechdel_target, not args.no_skills)


if __name__ == "__main__":
    main()
