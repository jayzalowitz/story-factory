# Site and README design decisions

The audience is a writer or producer who may never have used a coding assistant. The first page must answer what this makes, what to type, how to begin, what the real results look like, and who controls the decisions. Chapter navigation is extra depth, not a prerequisite for understanding the product.

## What stays consistent

Warm paper, dark green, restrained editorial typography and local fonts continue the existing site. Tinos carries large headings; Arimo handles instructions; the actual PDF pages show the readable screenplay/package typography. The hero uses real public Ledger Room pages instead of an invented sample. Those previews link to the actual PDFs and are labeled as demonstrations.

One command is the primary path. The first page includes host-specific copy buttons, setup/run/delivery steps, actual examples, the bounded review loop, explicit Bechdel/agency checks, current-version gates and finite-context explanation. GitHub is a persistent header link. Optional teams and fine-grained controls remain behind Advanced settings. The site sends/stores no story and loads its assets locally.

Mobile uses compact horizontally scrolling chapter links, a shorter title and a first-screen setup button. Decorative hero pages are omitted on small screens so the action comes first; the example links remain. Keyboard navigation and manual-copy recovery are preserved. Copy status is announced through a live region; copy-denied recovery focuses and selects the complete request.

## Inspiration, without copying implementations

- [gstack](https://github.com/garrytan/gstack): make the named workflow and practical starting request visible, then show the individual tools as optional depth.
- [Fountain](https://fountain.io/): introduce a writing tool in plain language and let concrete screenplay material demonstrate what it means.
- The project's own PDFs: use observable output as visual evidence, with provenance and scope; avoid invented testimonials or commercial claims.

The layout and code remain Story Factory's. No third-party product code, artwork, screenshots or branded components were imported.

## Actual review

Local browser checks cover desktop 1440×1000, phone 390×844, tablet 768×1024 and short laptop 1280×720. The landing page, one-command request, review gates and context explanation were inspected without horizontal overflow or console errors. Both host-specific clipboard paths and denied-copy selection recovery were exercised. Earlier chapter/deep-link/history/form checks remain covered separately. Screenshot evidence is local, outside the published artifact. Publishing and live-byte verification are separate final steps.
