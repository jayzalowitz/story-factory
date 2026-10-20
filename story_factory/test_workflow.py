"""Behavioral checks for sequencing, evidence, stale artifacts, and safe reopening."""
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import unittest


SOURCE = Path(__file__).resolve().parent


class WorkflowTests(unittest.TestCase):
    def setUp(self):
        self.temporary = tempfile.TemporaryDirectory()
        self.addCleanup(self.temporary.cleanup)
        self.root = Path(self.temporary.name)
        (self.root / "scripts").mkdir()
        shutil.copyfile(SOURCE / "workflow.py", self.root / "scripts/workflow.py")
        (self.root / "development").mkdir()

    def run_cli(self, *args):
        return subprocess.run([sys.executable, str(self.root / "scripts/workflow.py"), *args],
                              capture_output=True, text=True)

    def fill_discovery(self):
        for name in ("brief", "discovery"):
            (self.root / f"development/{name}.md").write_text(
                "# A specific story direction\n" + "A concrete protagonist pursues a difficult goal with an escalating cost. " * 3 +
                "\nVerdict: PASS\n")

    def test_missing_evidence_cannot_complete(self):
        result = self.run_cli("complete", "discover", "--evidence", "Reviewed the complete story direction.")
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("Missing:", result.stderr)

    def test_cannot_skip_discovery(self):
        result = self.run_cli("complete", "draft", "--evidence", "A complete readable draft is present.")
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("next stage is discover", result.stderr)

    def test_placeholder_or_failed_review_blocks(self):
        self.fill_discovery()
        report = self.root / "development/discovery.md"
        report.write_text(report.read_text().replace("Verdict: PASS", "Verdict: REVISE") + "DRAFT PLACEHOLDER")
        result = self.run_cli("check")
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("placeholder", result.stdout)
        self.assertIn("Verdict: PASS", result.stdout)

    def test_upstream_edit_invalidates_and_reopen_preserves_files(self):
        self.fill_discovery()
        self.assertEqual(self.run_cli("complete", "discover", "--evidence", "Reviewed direction and concrete story engine.").returncode, 0)
        self.assertIn("premise: NEXT", self.run_cli("status").stdout)
        brief = self.root / "development/brief.md"
        brief.write_text(brief.read_text() + "\nThe central relationship has changed.\n")
        self.assertIn("discover: STALE", self.run_cli("status").stdout)
        result = self.run_cli("complete", "premise", "--evidence", "Rechecked all premise risks and evidence.")
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("reopen discover", result.stderr)
        self.assertEqual(self.run_cli("reopen", "discover", "--reason", "The central relationship changed.").returncode, 0)
        self.assertIn("central relationship", brief.read_text())
        self.assertIn("discover: NEXT", self.run_cli("status").stdout)


if __name__ == "__main__":
    unittest.main()
