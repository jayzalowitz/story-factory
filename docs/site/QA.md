# Site evidence and review

Checked 2026-10-20 against the writer-friendly-site candidate. This report distinguishes local proof from public delivery. Public hosting has a separate approval gate.

## Scope and claims

The site introduces the existing story-development process to writers, creates an opening prompt locally, and offers copy/manual-copy/download. It does not run a model, write a screenplay on the site, promise professional outcomes, or expose the private repository. No external research or analytics was added. All example story text is fictional and labelled. No deck PDF companion, generator, or link was added; the pre-existing screenplay PDF tooling is separate and unchanged.

The execution brief, claim/preservation ledger, headline sequence, and design-plan review are in BRIEF.md. Under the deck skill's bounded adapter, design planning, visual audit, source review, QA, and documentation audit were covered by the parent with an independent same-host source reviewer. No separate specialist CLI invocation or external review is claimed.

## Automated and export checks

- `python3 -m unittest discover -s tests -v`: 5 tests pass. Checks local links/assets, unique chapter IDs, labels, public-file allowlist, no outbound/storage code, restrictive CSP, and the real text download.
- `python3 -m unittest discover -s story_factory -p 'test_*.py' -v`: 4 workflow tests pass.
- `node --check site/app.js`: pass. Node is a check tool only, not a site runtime dependency.
- A fresh export to a temporary directory preserved the complete workflow and produced a writer-friendly README.
- Markdown relative-link check: no broken links.
- Existing LaTeX layouts, fonts, and screenplay/package inputs were not changed, so the prior successful 18-PDF build remains evidence for those unchanged inputs; it was not rerun as a site test.

## Real-browser behavior

The in-app browser was unavailable; the installed gstack Chromium browser provided the live browser proof. Loopback-only HTTP servers served the exact static artifact. Synthetic story notes only; no user story was submitted to a service.

Passed: valid direct chapter links and refresh; invalid-fragment fallback; stripping incoming tracking queries; back and forward synchronization; tab roles/selection; Arrow keys, Home, End, Space, and focus; next/previous controls; skip link to the active panel; input keys that never change chapters; empty-idea error and focus recovery; literal script-like input staying text; idea-stage and existing-draft prompts; example fill; refresh clearing unsaved notes; local prompt download; and static starter download returning text/plain.

Clipboard success and permission-denied paths were exercised with a simulated browser clipboard object, without touching the user's system clipboard. The denied path selects the prompt and gives manual-copy/download guidance. No claim is made that every browser grants automatic clipboard access.

Page-load resources remained local to the loopback origin. Browser console reported no errors. A second static preview served the artifact at `/story-factory/`; HTML, CSS, JavaScript, all fonts, favicon, and starter returned HTTP 200 with appropriate types. Direct `#start` and skip-link behavior worked at that prefix. No development-router fallback was used.

The no-JavaScript reading/download fallback was source-reviewed: chapters are not hidden in HTML, navigation links are real fragments, and a noscript download path exists. Disabling script execution through the browser tool was denied by its CDP allowlist; an actual script-disabled browser run is therefore not claimed.

## Visual proof

All five chapters were captured at both top and available bottom at these exact viewports:

| Device composition | Width × height |
|---|---|
| Desktop | 1440 × 1000 |
| Phone | 390 × 844 |
| Tablet | 768 × 1024 |
| Short laptop | 1280 × 720 |

That is 40 viewport captures, plus interaction and prefix proof. Each layout had no horizontal overflow and a reachable bottom. Screenshots/contact sheets were inspected for hierarchy, density, readable copy, forms, wrapping, controls, and clipped required content. Meaningful fixes enlarged small instructions, increased mobile navigation targets, and moved the example disclaimer below the art into normal flow. Body copy is 16px; forms use 16px input text. Decorative screenplay text is intentionally smaller and is not required information.

Private workspace artifacts: `.context/story-site-proof/` with `{device}-{chapter}-{top|bottom}.png`, matrix.json, and console.txt; `.context/story-site-browser-check.py` and its log record repeatable assertions. Screenshots and private review material are not part of the public site allowlist.

## Independent review and documentation

A fresh-context reviewer on the current agent host reviewed the source, safety boundaries, beginner copy, export behavior, and publication workflow. It independently reran 5 site tests, 4 workflow tests, and the JavaScript syntax check. No remaining actionable findings. Its optional public-artifact allowlist recommendation was implemented and re-reviewed. The final art-caption layout change was also re-reviewed.

Copilot and external model review were not requested because new external processing was not approved. No Copilot result is claimed.

Documentation coverage: README provides the plain-language entry and starter conversation; WRITING_GUIDE.md is the beginner tutorial; docs/SETUP.md retains the technical reference; docs/site/README.md explains preview, browser assertions, publishing, and rollback; CONTRIBUTING.md covers site tests and the public allowlist. The exporter now gives new projects a writer-friendly README as well. No configured version file or changelog existed, so none was invented.
