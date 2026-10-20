# The Pool — a completed inspired-by short

Two longtime musicians meet in an empty swimming pool to record a last duet before one moves away. Keeping an imperfect recording requires the other to accept both her own voice and her partner's departure.

Read the [complete screenplay](screenplay/the-pool.fountain), [truth audit](research/truth_report.md), [claim ledger](research/claims.json) and [targeted craft review](development/quality_report.md). The selected PDF is `output/the-pool.pdf`: six physical pages, including the cover, with five dramatic pages. It was actually built with Tectonic; the final pages were rendered for visual inspection. No package or pitch documents were selected.

The seed is precise and limited: an [inspected NPS historical account](https://www.nps.gov/places/000/first-flight-landing.htm) describes how short and modest the first flight was. The author borrowed the idea that a small first achievement can matter. Every person, location, musical event and private exchange here is invented. This is not the story of real musicians, and the early-flight citation cannot justify marketing it as one.

This is an actual second completed screenplay, contrasting with [Twelve Seconds](../../adaptation/README.md), which preserves documented historical people and event facts. It uses a different setting, relationship and action rather than simply renaming historical figures.

Run the local evidence checks from the repository root:

```
python3 examples/true-story/inspired-by/check_promises.py
tectonic --outdir examples/true-story/inspired-by/output examples/true-story/inspired-by/screenplay/the-pool.tex
```

The first command checks current truth/craft receipts and demonstrates rejection of the explicitly recorded false based-on label. The semantic judgment belongs to the reviewer; a script cannot independently determine whether a story really happened. All reviews were by the authoring agent; no human, separate agent or external model was used in this bounded contrast. No new research was performed. Fountain and TeX are the paired readable/typeset sources and must both be updated before a revised build and review.
