# The public introduction

The website lives in `site/`. It is plain HTML, CSS, and browser JavaScript, with bundled fonts. It has no accounts, AI connection, analytics, form submission, remote assets, or story storage. Its only generated content is an opening prompt assembled in the visitor's browser. Writing happens in the visitor's chosen AI assistant.

Preview from the repository root:

```sh
python3 -m http.server 8765 --bind 127.0.0.1 --directory site
```

Open `http://127.0.0.1:8765/`. The exact contents of site/ are the publishable artifact; never deploy the repository root. Chapter links use fragments so direct entry and refresh work without server rewrites. Without JavaScript, all chapters remain readable and the static starter prompt can still be downloaded.

Content sources: README.md, WRITING_GUIDE.md, WORKFLOW.md, and MASTER_PROMPT.md. The standalone chat starter in site/story-starter.txt is a deliberately shorter, nontechnical entry point. It does not claim to run the complete file-based workflow. There is no deck PDF companion or export-PDF feature.

## Publishing, only after confirmation

The prepared GitHub Actions workflow is manual only. No push or pull request publishes the site. Before enabling Pages or running the workflow, confirm the exact public destination and that only site/ will be exposed. Keep the source repository private. GitHub account eligibility for public Pages from a private repository must be verified before setup.

Proposed destination: `https://jayzalowitz.github.io/story-factory/`.

After approval, configure Pages with GitHub Actions as its source and run the “Publish introduction” workflow from the approved main commit. The workflow uploads site/ only. Verify live chapter links, CSS/fonts, downloads, copy/fallback behavior, and no nonlocal page-load requests apart from the selected host. Roll back by redeploying an earlier site commit or disabling Pages; neither requires making the repository public. No custom domain, DNS, paid host, or analytics configuration is part of this change.

## Checks

```sh
python3 -m unittest discover -s tests -v
python3 -m unittest discover -s story_factory -p 'test_*.py' -v
node --check site/app.js
```

Node is an optional local syntax check, not a requirement to serve or use the site. Native Python tests check public artifact isolation, local links/resources, navigation structure, privacy restrictions, and the downloadable starter. Browser QA additionally covers deep links, history, tab keyboard behavior, typing without navigation, empty/error recovery, generated prompts, copy success/fallback, and downloads. Inspect desktop, phone, tablet, and short-height layouts for every chapter and its bottom state. Evidence belongs in the private workspace; record results in QA.md without embedding private user stories.

See [the execution brief](BRIEF.md) and [verification record](QA.md) for the implementation decisions and evidence.
