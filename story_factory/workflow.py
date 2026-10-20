#!/usr/bin/env python3
"""Track the artifact-backed story workflow. Does not generate or judge stories."""
import argparse
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
STATE = ROOT / "development/workflow.json"
STAGES = {
    "discover": (["development/brief.md", "development/discovery.md"], "development/discovery.md"),
    "premise": (["development/story_bible.md", "development/premise_review.md"], "development/premise_review.md"),
    "structure": (["development/outline.md", "development/scene_map.md", "development/continuity.md", "development/structure_review.md"], "development/structure_review.md"),
    "draft": (["screenplay/*.tex", "development/draft_report.md"], "development/draft_report.md"),
    "revise": (["development/review.md", "development/revision_log.md"], "development/review.md"),
    "package": (["package/*.tex", "one_pagers/*.tex", "development/package_review.md"], "development/package_review.md"),
    "verify": (["development/verification.md", "common/*.tex", "Makefile", "latexmkrc"], "development/verification.md"),
    "handoff": (["README.md", "development/status.md", "development/handoff.md"], "development/handoff.md"),
}
MARKERS = re.compile(r"DRAFT PLACEHOLDER|TO BE (?:PROVIDED|DEVELOPED|WRITTEN)|\bTODO\b|\bTBD\b", re.I)


def artifacts(stage):
    files = {}
    problems = []
    for pattern in STAGES[stage][0]:
        matches = sorted(ROOT.glob(pattern))
        if not matches:
            problems.append(f"Missing: {pattern}")
        for path in matches:
            name = path.relative_to(ROOT).as_posix()
            content = path.read_text(encoding="utf-8")
            prose = "\n".join(line for line in content.splitlines() if not line.lstrip().startswith("%"))
            if len(prose.strip()) < 80 or MARKERS.search(prose):
                problems.append(f"Incomplete or placeholder: {name}")
            files[name] = hashlib.sha256(path.read_bytes()).hexdigest()
    report = ROOT / STAGES[stage][1]
    if report.exists() and not re.search(r"^Verdict:\s*PASS\s*$", report.read_text(), re.M):
        problems.append(f"Review must explicitly record Verdict: PASS: {report.relative_to(ROOT)}")
    return files, problems


def current(receipts):
    for stage in STAGES:
        if stage not in receipts:
            return stage, False
        files, problems = artifacts(stage)
        if problems or files != receipts[stage]["files"]:
            return stage, True
    return None, False


def save(receipts):
    STATE.parent.mkdir(parents=True, exist_ok=True)
    temporary = STATE.with_suffix(".tmp")
    temporary.write_text(json.dumps({"schema": 1, "completed": receipts}, indent=2) + "\n")
    temporary.replace(STATE)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest="command", required=True)
    sub.add_parser("status")
    sub.add_parser("check")
    complete = sub.add_parser("complete")
    complete.add_argument("stage", choices=STAGES)
    complete.add_argument("--evidence", required=True)
    reopen = sub.add_parser("reopen")
    reopen.add_argument("stage", choices=STAGES)
    reopen.add_argument("--reason", required=True)
    args = parser.parse_args()
    receipts = json.loads(STATE.read_text())["completed"] if STATE.exists() else {}
    stage, stale = current(receipts)
    if args.command in ("status", "check"):
        for name in STAGES:
            label = "complete" if name in receipts else "pending"
            if name == stage:
                label = "STALE; reopen required" if stale else "NEXT"
            elif stage and list(STAGES).index(name) > list(STAGES).index(stage):
                label = "pending revalidation" if name in receipts else "pending"
            print(f"{name}: {label}")
        if stage:
            print(f"Next: read WORKFLOW.md stage '{stage}'.")
        if args.command == "check" and stage:
            _, problems = artifacts(stage)
            print("\n".join(problems) if problems else "Artifacts present; editorial verdict and evidence still require judgment.")
            raise SystemExit(1 if stale or problems else 0)
        return
    if args.command == "reopen":
        if len(args.reason.strip()) < 12:
            parser.error("give a concrete reason (at least 12 characters)")
        start = list(STAGES).index(args.stage)
        receipts = {name: value for name, value in receipts.items() if list(STAGES).index(name) < start}
        save(receipts)
        with (ROOT / "development/workflow-events.jsonl").open("a") as stream:
            stream.write(json.dumps({"event": "reopen", "stage": args.stage, "reason": args.reason,
                                     "time": datetime.now(timezone.utc).isoformat()}) + "\n")
        print(f"Reopened {args.stage} and all later stages; creative files preserved.")
        return
    if stale:
        parser.error(f"completed artifacts changed; reopen {stage} first")
    if args.stage != stage:
        parser.error(f"complete stages in order; next stage is {stage or 'none'}")
    if len(args.evidence.strip()) < 20:
        parser.error("provide a concrete evidence summary (at least 20 characters)")
    files, problems = artifacts(stage)
    if problems:
        parser.error("\n".join(problems))
    receipts[stage] = {"files": files, "evidence": args.evidence,
                       "time": datetime.now(timezone.utc).isoformat()}
    save(receipts)
    print(f"Recorded {stage}. Run status for the next stage.")


if __name__ == "__main__":
    main()
