"""Validate optional native helper plans and recorded activity; never launch workers."""
from __future__ import annotations
import argparse
import hashlib
from datetime import datetime
import json
from pathlib import Path

TASKS = {"research", "continuity", "quality", "package-review"}
DEFAULTS = {"mode": "off", "max_workers": 3, "max_rounds": 1,
            "max_sources_per_worker": 10, "allowed_tasks": sorted(TASKS),
            "allow_nested": False, "new_paid_services": False}

class TeamError(ValueError):
    pass

def integer(value, minimum, maximum):
    return type(value) is int and minimum <= value <= maximum

def validate_settings(settings):
    if not isinstance(settings, dict) or set(settings) != set(DEFAULTS):
        raise TeamError("Team settings require exactly the documented fields; use sequential work until corrected.")
    if settings["mode"] not in ("off", "ask", "auto"):
        raise TeamError("Team mode must be off, ask or auto.")
    for name, low, high in (("max_workers", 1, 3), ("max_rounds", 1, 3), ("max_sources_per_worker", 1, 20)):
        if not integer(settings[name], low, high):
            raise TeamError(f"{name} must be an integer from {low} to {high}.")
    tasks = settings["allowed_tasks"]
    if not isinstance(tasks, list) or any(not isinstance(t, str) for t in tasks) or len(tasks) != len(set(tasks)) or not set(tasks) <= TASKS:
        raise TeamError("Allowed tasks must be a unique list of documented review/research tasks.")
    if settings["allow_nested"] is not False or settings["new_paid_services"] is not False:
        raise TeamError("Nested teams and new paid providers are unsupported.")
    return settings

def timestamp(value):
    if not isinstance(value, str):
        raise TeamError("Record approval and launch timestamps with timezone.")
    try:
        parsed = datetime.fromisoformat(value.replace("Z", "+00:00"))
    except ValueError as exc:
        raise TeamError("Record valid approval and launch timestamps.") from exc
    if parsed.tzinfo is None:
        raise TeamError("Activity timestamps require a timezone.")
    return parsed

def digest(value):
    return hashlib.sha256(json.dumps(value, sort_keys=True, separators=(",", ":")).encode()).hexdigest()

def validate_plan(settings, plan):
    validate_settings(settings)
    if not isinstance(plan, dict):
        raise TeamError("Team plan must be an object.")
    if plan.get("settings_sha256") != digest(settings):
        raise TeamError("Plan settings are stale; regenerate the plan.")
    if not isinstance(plan.get("objective"), str) or not plan["objective"].strip() or not isinstance(plan.get("draft_fingerprint"), str) or not plan["draft_fingerprint"].strip():
        raise TeamError("Record the objective and exact draft fingerprint.")
    workers = plan.get("workers")
    if not isinstance(workers, list) or len(workers) > settings["max_workers"]:
        raise TeamError("Worker count exceeds the configured cap.")
    if workers and settings["mode"] == "off":
        raise TeamError("Teams are off. Complete the passes sequentially.")
    capability = plan.get("capability", {})
    if workers and (not isinstance(capability, dict) or capability.get("native_available") is not True or not isinstance(capability.get("observed_tool"), str) or not capability["observed_tool"].strip() or not isinstance(capability.get("observed_at"), str) or not capability["observed_at"].strip() or not isinstance(capability.get("session_id"), str) or not capability["session_id"].strip()):
        raise TeamError("Record the actual native tool observed in this session, not a subscription or brand assumption.")
    names = set()
    for worker in workers:
        if not isinstance(worker, dict):
            raise TeamError("Each worker must be an object.")
        name = worker.get("name")
        if not isinstance(name, str) or not name or name in names:
            raise TeamError("Workers require unique names.")
        names.add(name)
        if worker.get("task") not in settings["allowed_tasks"]:
            raise TeamError("Worker task is not permitted.")
        if not integer(worker.get("rounds"), 1, settings["max_rounds"]) or not integer(worker.get("source_limit"), 0, settings["max_sources_per_worker"]):
            raise TeamError("Worker round or source limit exceeds settings.")
        path = worker.get("output_path")
        if not isinstance(path, str) or Path(path).is_absolute() or ".." in Path(path).parts or not path.startswith("development/workers/") or len(Path(path).parts) < 3:
            raise TeamError("Worker output must stay in its assigned development/workers notes directory.")
        if worker.get("allow_nested") is not False or worker.get("script_write") is not False:
            raise TeamError("Only the coordinator may write story canon; workers cannot delegate.")
    paths = [Path(w["output_path"]) for w in workers]
    if any(a == b or a in b.parents or b in a.parents for i, a in enumerate(paths) for b in paths[i+1:]):
        raise TeamError("Workers must have disjoint notes directories.")
    return plan

def authorize_plan(settings, plan, approval=None, current_session=None):
    """Preflight recorded permission before launch; host tools remain outside this checker."""
    validate_plan(settings, plan)
    if not plan["workers"]:
        return {"status": "SEQUENTIAL", "worker_count": 0}
    if not current_session or plan["capability"]["session_id"] != current_session:
        raise TeamError("Re-observe the native tool in this current session before launch.")
    if settings["mode"] == "ask":
        if not isinstance(approval, dict) or approval.get("approved") is not True or approval.get("plan_sha256") != digest(plan) or not isinstance(approval.get("evidence"), str) or not approval["evidence"].strip():
            raise TeamError("Wait for the writer's approval of this exact plan before launch.")
        timestamp(approval.get("approved_at"))
    return {"status": "RECORDED_PREFLIGHT_VALID", "worker_count": len(plan["workers"]), "plan_sha256": digest(plan)}

def check_activity(settings, plan, receipt):
    validate_plan(settings, plan)
    if not isinstance(receipt, dict) or receipt.get("plan_sha256") != digest(plan):
        raise TeamError("Activity receipt does not match the exact plan.")
    workers = {w["name"]: w for w in plan["workers"]}
    activity = receipt.get("launches")
    if not isinstance(activity, list):
        raise TeamError("Receipt requires actual launch records, including an empty list when no helpers ran.")
    if settings["mode"] == "off" and activity:
        raise TeamError("Helpers were launched while teams were off.")
    approval = receipt.get("approval", {})
    if settings["mode"] == "ask" and activity and (not isinstance(approval, dict) or approval.get("plan_sha256") != digest(plan) or approval.get("approved") is not True or not isinstance(approval.get("evidence"), str) or not approval["evidence"].strip()):
        raise TeamError("Ask-first mode requires recorded writer approval of this exact plan before launch.")
    seen = set()
    for launch in activity:
        if not isinstance(launch, dict) or launch.get("worker") not in workers:
            raise TeamError("Unplanned worker recorded.")
        worker = workers[launch["worker"]]
        launched_at = timestamp(launch.get("launched_at"))
        if settings["mode"] == "ask" and timestamp(approval.get("approved_at")) > launched_at:
            raise TeamError("Approval must precede every launch.")
        round_number = launch.get("round")
        if not integer(round_number, 1, worker["rounds"]):
            raise TeamError("Unplanned round recorded.")
        key = (launch["worker"], round_number)
        if key in seen:
            raise TeamError("Duplicate worker round recorded.")
        seen.add(key)
        if not isinstance(launch.get("native_launch_id"), str) or not launch["native_launch_id"].strip():
            raise TeamError("Record the actual native launch identifier.")
        if not integer(launch.get("sources_inspected"), 0, worker["source_limit"]):
            raise TeamError("Source count exceeds assignment.")
        if launch.get("nested_launches") != 0 or type(launch.get("nested_launches")) is not int or launch.get("script_writes") is not False or launch.get("new_paid_services") is not False:
            raise TeamError("Receipt reports unsupported delegation, story writes or new paid services.")
    if len({item[0] for item in seen}) > settings["max_workers"]:
        raise TeamError("Actual worker count exceeds the configured cap.")
    return {"status": "VALID_RECORDED_ACTIVITY", "actual_launches": len(activity),
            "actual_workers": len({item[0] for item in seen}),
            "usage": receipt.get("usage", "unknown"),
            "limitation": "Validates supplied records; does not monitor or enforce host tool calls or dollar spend."}

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--project", type=Path, default=Path.cwd())
    parser.add_argument("action", choices=("settings", "plan", "authorize", "activity"))
    parser.add_argument("--session", help="Current native session identifier observed by the coordinator")
    args = parser.parse_args()
    root = args.project / "development"
    try:
        config = json.loads((root / "teams.json").read_text()) if (root / "teams.json").exists() else dict(DEFAULTS)
        validate_settings(config)
        if args.action == "settings":
            result = {"settings": config, "settings_sha256": digest(config)}
        else:
            plan = json.loads((root / "team_plan.json").read_text())
            validate_plan(config, plan)
            result = {"status": "VALID_PLAN", "plan_sha256": digest(plan)}
            if args.action == "authorize":
                approval_file = root / "team_approval.json"
                approval = json.loads(approval_file.read_text()) if approval_file.exists() else None
                result = authorize_plan(config, plan, approval, args.session)
            if args.action == "activity":
                result = check_activity(config, plan, json.loads((root / "team_activity.json").read_text()))
        print(json.dumps(result, indent=2))
        return 0
    except (TeamError, OSError, ValueError, TypeError) as exc:
        print(f"Team controls: {exc}")
        return 1

if __name__ == "__main__":
    raise SystemExit(main())
