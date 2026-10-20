import copy
import unittest
from story_factory.team_controls import DEFAULTS, TeamError, authorize_plan, check_activity, digest, validate_plan, validate_settings

class TeamControlsTests(unittest.TestCase):
    def fixture(self, mode="auto"):
        settings = copy.deepcopy(DEFAULTS)
        settings["mode"] = mode
        plan = {"settings_sha256": digest(settings), "objective": "Review prop continuity", "draft_fingerprint": "draft-sha",
                "capability": {"native_available": True, "observed_tool": "native.spawn", "observed_at": "2026-10-20T12:00:00Z", "session_id": "current-test-session"},
                "workers": [{"name": "continuity", "task": "continuity", "rounds": 1, "source_limit": 0,
                             "output_path": "development/workers/continuity", "allow_nested": False, "script_write": False}]}
        receipt = {"plan_sha256": digest(plan), "launches": [{"worker": "continuity", "round": 1, "native_launch_id": "test-launch", "launched_at": "2026-10-20T12:02:00Z", "sources_inspected": 0, "nested_launches": 0, "script_writes": False, "new_paid_services": False}]}
        return settings, plan, receipt

    def test_supported_bounds_and_false_flags(self):
        for key, value in (("max_workers", 4), ("max_rounds", True), ("max_sources_per_worker", 21), ("allow_nested", 0), ("new_paid_services", True), ("allowed_tasks", ["rewrite"])):
            settings = copy.deepcopy(DEFAULTS)
            settings[key] = value
            with self.subTest(key=key), self.assertRaises(TeamError):
                validate_settings(settings)

    def test_off_has_no_helpers(self):
        settings, plan, receipt = self.fixture("off")
        with self.assertRaises(TeamError):
            validate_plan(settings, plan)
        plan["workers"] = []
        receipt["plan_sha256"] = digest(plan)
        with self.assertRaises(TeamError):
            check_activity(settings, plan, receipt)
        receipt["launches"] = []
        self.assertEqual(check_activity(settings, plan, receipt)["actual_workers"], 0)

    def test_ask_requires_exact_plan_approval(self):
        settings, plan, receipt = self.fixture("ask")
        with self.assertRaises(TeamError):
            check_activity(settings, plan, receipt)
        receipt["approval"] = {"approved": True, "approved_at": "2026-10-20T12:01:00Z", "plan_sha256": digest(plan), "evidence": "Writer approved this exact continuity assignment."}
        self.assertEqual(check_activity(settings, plan, receipt)["actual_workers"], 1)
        receipt["approval"]["plan_sha256"] = "old-plan"
        with self.assertRaises(TeamError):
            check_activity(settings, plan, receipt)

    def test_auto_requires_observed_native_capability(self):
        settings, plan, receipt = self.fixture()
        self.assertEqual(check_activity(settings, plan, receipt)["usage"], "unknown")
        plan["capability"] = {"subscription": "paid"}
        with self.assertRaises(TeamError):
            validate_plan(settings, plan)

    def test_activity_limits_and_unplanned_workers(self):
        for key, value in (("worker", "surprise"), ("round", 2), ("sources_inspected", 1), ("nested_launches", 1), ("script_writes", True), ("new_paid_services", True)):
            settings, plan, receipt = self.fixture()
            receipt["launches"][0][key] = value
            with self.subTest(key=key), self.assertRaises(TeamError):
                check_activity(settings, plan, receipt)
        settings, plan, receipt = self.fixture()
        receipt["launches"] *= 2
        with self.assertRaises(TeamError):
            check_activity(settings, plan, receipt)

    def test_prelaunch_permission_and_current_session(self):
        settings, plan, receipt = self.fixture("ask")
        with self.assertRaises(TeamError):
            authorize_plan(settings, plan, current_session="current-test-session")
        approval = {"approved": True, "approved_at": "2026-10-20T12:01:00Z", "plan_sha256": digest(plan), "evidence": "Writer approved exact assignment."}
        with self.assertRaises(TeamError):
            authorize_plan(settings, plan, approval, "different-session")
        self.assertEqual(authorize_plan(settings, plan, approval, "current-test-session")["worker_count"], 1)
        settings, plan, receipt = self.fixture("auto")
        self.assertEqual(authorize_plan(settings, plan, current_session="current-test-session")["worker_count"], 1)

    def test_approval_cannot_follow_launch(self):
        settings, plan, receipt = self.fixture("ask")
        receipt["approval"] = {"approved": True, "approved_at": "2026-10-20T12:03:00Z", "plan_sha256": digest(plan), "evidence": "Late approval"}
        with self.assertRaises(TeamError):
            check_activity(settings, plan, receipt)

    def test_settings_or_plan_changes_stale_records(self):
        settings, plan, receipt = self.fixture()
        settings["max_rounds"] = 2
        with self.assertRaises(TeamError):
            check_activity(settings, plan, receipt)
        plan["settings_sha256"] = digest(settings)
        with self.assertRaises(TeamError):
            check_activity(settings, plan, receipt)

    def test_mirror_is_identical(self):
        from pathlib import Path
        root = Path(__file__).resolve().parents[1]
        self.assertEqual((root / "scripts/team_controls.py").read_bytes(), (root / "story_factory/team_controls.py").read_bytes())

    def test_worker_paths_disjoint_and_coordinator_only_writes(self):
        settings, plan, receipt = self.fixture()
        second = dict(plan["workers"][0], name="other", output_path="development/workers/continuity/nested")
        plan["workers"].append(second)
        with self.assertRaises(TeamError):
            validate_plan(settings, plan)
        plan["workers"].pop()
        plan["workers"][0]["output_path"] = "development/workers/../../screenplay"
        with self.assertRaises(TeamError):
            validate_plan(settings, plan)

if __name__ == "__main__":
    unittest.main()
