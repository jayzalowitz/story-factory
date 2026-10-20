# Relocated build evidence

This document records a real rebuild of this curated example, not runtime workflow completion state. The host agent executed `make -B all` here using local Tectonic after changing the typography font references to `../../../fonts/`. After adding the second-reader note to the package appendix, `make -B package` rebuilt that document. Both commands exited successfully; no warning, overfull-box or error lines were found in either local build log. Operational logs and temporary render files stay in ignored `output/` and are not published.

All eighteen resulting PDFs were copied deliberately from `output/` into `pdfs/` and measured with Poppler `pdfinfo`. File hashes and measured counts are in pdf_inventory.json. The screenplay is ten total PDF pages: one title and nine dramatic pages; no movement dividers. Package is seventeen pages including title and contents. Sixteen pitches are exactly one actual page each at unchanged readable typography.

| PDF | Pages |
|---|---:|
| actor-pitch.pdf | 1 |
| awards-pitch.pdf | 1 |
| coproduction-pitch.pdf | 1 |
| craft-pitch.pdf | 1 |
| cultural-partnership-pitch.pdf | 1 |
| director-pitch.pdf | 1 |
| distributor-pitch.pdf | 1 |
| exhibitor-pitch.pdf | 1 |
| festival-pitch.pdf | 1 |
| financier-pitch.pdf | 1 |
| one-pager.pdf | 1 |
| press-pitch.pdf | 1 |
| producer-pitch.pdf | 1 |
| public-funder-pitch.pdf | 1 |
| screenplay.pdf | 10 |
| streamer-pitch.pdf | 1 |
| studio-package.pdf | 17 |
| talent-rep-pitch.pdf | 1 |

The repository's native helper source and quality checks were run against this relocated example and passed. The current draft fingerprint in quality.json and bechdel.json covers all screenplay source files. Those are writing-agent editorial receipts, not an automated quality score. No relocated runtime workflow.json or stage-completion records are supplied.

Visual evidence: during the original host-agent run, every screenplay, package and pitch page was rendered and its contact sheets inspected by the writing agent. A second host agent read the entire screenplay and contact sheets. Following relocation, the writing agent rendered and inspected the opening, costly-choice and ending screenplay pages, the updated package appendix and the actor pitch. Readable cues/dialogue, page numbers, margins and paragraph endings were observed; no clipping or overlap seen. Root fonts preserve the original metrics and no layout/font substitution warning occurred. This is assisted visual checking, not a printer proof or a native Claude-host test.

Actual original-run repairs are preserved in revision_log.md and first-draft/. An initial overfull-box diagnosis was wrong; shortening the actual dialogue line and making the written correction sentence case fixed the warnings. An intervening original build was correctly rejected when its source bytes changed; that was a guard functioning, not a toolkit defect. These historic observations are not new relocated workflow receipts.

Remaining limits: invented compressed contract mechanics; runtime untested; no live performance/camera test; final relabeling may feel neat. No external services, submissions, outreach, production, legal/financial validation or awards/finance guarantee. This short demonstration is not proof of feature-quality guarantees.
