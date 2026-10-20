# Choose your finished materials

Every item is optional. Tell the assistant what you need in ordinary language. You can request only a screenplay, a small set of development pages, a single pitch, or the complete package. A full selection produces 18 PDFs: the screenplay, one book containing the selected development sections, and sixteen separate one-page pitches. Research/review notes are working evidence, not extra mandatory sales documents.

## Development package sections

- Logline and Synopses
- Treatment
- Character Breakdowns
- Tone and Visual World
- Comparables and Positioning
- Casting Proposals
- Director Targets
- Producer Targets
- Awards Strategy
- Festival Strategy
- Budget and Production Scope
- Scene Showcase
- Marketing Description
- Taglines
- Risks, Research, Rights, and Next Steps

## Reader-specific one-page pitches

- General Pitch
- Actor Pitch
- Director Pitch
- Financier Pitch
- Producer Pitch
- Distributor Pitch
- Streamer Pitch
- Festival Pitch
- Awards Pitch
- Co-production Pitch
- Public Funder Pitch
- Talent Representative Pitch
- Exhibitor Pitch
- Cultural Partnership Pitch
- Press Pitch
- Craft Department Pitch

## How to ask

> Make a screenplay, synopsis, treatment, character descriptions, and a director pitch. Skip everything else.

Your assistant records the selection in development/package_options.json. All available choices are initially selected in a new project; change them before packaging. Unselected templates can stay blank and do not block a selected build. Selecting a budget or awards page does not make estimates true or a campaign real. Every claim still needs honest qualification.

For a helper using the terminal:

```sh
python3 scripts/package_options.py list
python3 scripts/package_options.py configure --section logline_synopsis --section treatment --section character_breakdowns --pitch director_pitch
python3 scripts/story_check.py build
```

`configure` replaces each section or pitch list only when its flags are supplied; omitted lists keep their current selection. Use `--no-sections` or `--no-pitches` to choose none. Screenplay keeps its current setting unless `--with-screenplay` or `--without-screenplay` is supplied (initially selected). At least one output must remain. `show` prints the saved choice. `make all` builds every template; use `story_check.py build` to honor your selection and record verified outputs. A selection change makes earlier package/build receipts stale until checked again. Omitted full-project writing stages are never marked complete just to make a partial request look finished.
