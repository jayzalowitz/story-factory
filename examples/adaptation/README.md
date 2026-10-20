# Twelve Seconds — a worked historical adaptation

A complete compact short turns three short National Park Service historical accounts into six screenplay pages plus a cover. Read the [finished PDF](../../site/examples/adaptation/twelve-seconds.pdf), [screenplay](screenplay/twelve-seconds.fountain), [source notes](sources/nps-reading-notes.md), [decisions and scene map](adaptation/project.json), and [review](adaptation/review.md).

This was written in this implementation session, not extracted from the earlier feature. The authoring agent chose and approved the demonstration brief; no user interview or independent editorial panel is implied. The source pages were actually opened and read. They are institutional retrospective accounts from one organization, not independent primary witnesses. An inaccessible original archive is explicitly excluded. The film uses historical facts with original action and dialogue, not a copied source screenplay or a third-party framework.

The story keeps the documented experiment while inventing private exchanges. It does not quote the original telegram. The [truth-promise comparison](../true-story/README.md) explains what would need to change for a fictional inspired-by version. The research ledger includes verified event facts, an inferred motive, invented dialogue and an unresolved source ambiguity that was omitted from the script.

Selected delivery: screenplay only. No studio package or pitch PDF is claimed. `output/twelve-seconds.pdf` was built with Tectonic (7 pages: cover + 6 script pages). To rebuild from the repository root:

```
tectonic --outdir examples/adaptation/output examples/adaptation/screenplay/twelve-seconds.tex
python3 scripts/adaptation.py current --project examples/adaptation
python3 scripts/story_check.py truth-current --project examples/adaptation
```

The Fountain text is the readable source; the TeX file is its current typeset counterpart. An edit must update both before rebuilding and rereviewing. This small example does not prove feature-length continuity, native Claude/Codex execution, beginner usability or identical artistic outcomes. The full-draft craft review remains an authoring-agent review. Bechdel result is FAIL: no named women speak. The example reports that honestly instead of inserting an unrelated exchange.
