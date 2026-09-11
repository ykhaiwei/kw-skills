from datetime import datetime, timedelta, timezone
import importlib.util
import json
from pathlib import Path
import subprocess
import tempfile
import unittest


ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    "kw_upstream", ROOT / "skills/kw-mode/scripts/check_upstream.py")
upstream = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(upstream)


class UpstreamTests(unittest.TestCase):
    def setUp(self):
        temporary = tempfile.TemporaryDirectory()
        self.addCleanup(temporary.cleanup)
        self.root = Path(temporary.name)
        self.source = self.root / "source"
        self.source.mkdir()
        self.git("init", "-b", "main")
        self.git("config", "user.name", "Test")
        self.git("config", "user.email", "test@example.invalid")
        manifest = self.source / "pstack/.cursor-plugin/plugin.json"
        manifest.parent.mkdir(parents=True)
        manifest.write_text('{"version": "1.0"}')
        (self.source / "pstack/old.md").write_text("original\n")
        self.base = self.commit()
        self.hub = self.root / "hub"
        self.hub.mkdir()
        self.provenance = json.dumps({"repository": str(self.source), "commit": self.base})
        (self.hub / "upstream.json").write_text(self.provenance)
        self.now = datetime(2026, 9, 11, tzinfo=timezone.utc)

    def git(self, *args):
        return subprocess.run(["git", "-C", str(self.source), *args], check=True,
                              capture_output=True, text=True).stdout.strip()

    def commit(self):
        self.git("add", ".")
        self.git("commit", "-m", "fixture")
        return self.git("rev-parse", "HEAD")

    def test_scans_new_and_deleted_files_without_importing(self):
        (self.source / "pstack/old.md").unlink()
        (self.source / "pstack/new.md").write_text("new useful idea\n")
        head = self.commit()
        result = upstream.scan(self.hub, now=self.now)
        self.assertEqual(result["status"], "checked")
        self.assertEqual(result["head"], head)
        self.assertTrue(result["review_required"])
        self.assertEqual(result["changes"], ["A\tpstack/new.md", "D\tpstack/old.md"])
        self.assertIn("+new useful idea", Path(result["diff_path"]).read_text())
        self.assertEqual((self.hub / "upstream.json").read_text(), self.provenance)
        self.assertFalse((self.hub / "skills").exists())

    def test_cached_check_works_offline_and_due_failure_preserves_success(self):
        upstream.scan(self.hub, now=self.now)
        self.source.rename(self.root / "offline")
        fresh = upstream.scan(self.hub, now=self.now + timedelta(days=6))
        self.assertEqual(fresh["status"], "fresh")
        failed = upstream.scan(self.hub, now=self.now + timedelta(days=7))
        self.assertEqual(failed["status"], "error")
        saved = json.loads((self.hub / ".kw-state/upstream/state.json").read_text())
        self.assertEqual(saved["checked_at"], self.now.isoformat())
        retry = upstream.scan(self.hub, now=self.now + timedelta(days=7, hours=1))
        self.assertEqual(retry["status"], "retry_later")
        forced = upstream.scan(self.hub, force=True, now=self.now + timedelta(days=7, hours=2))
        self.assertEqual(forced["status"], "error")

    def test_forced_check_finds_changes_before_week_is_up(self):
        upstream.scan(self.hub, now=self.now)
        (self.source / "pstack/old.md").write_text("changed\n")
        head = self.commit()
        cached = upstream.scan(self.hub, now=self.now + timedelta(hours=1))
        self.assertFalse(cached["review_required"])
        forced = upstream.scan(self.hub, force=True, now=self.now + timedelta(hours=1))
        self.assertTrue(forced["review_required"])
        self.assertEqual(forced["head"], head)

    def test_completed_review_consumes_pending_report(self):
        (self.source / "pstack/old.md").write_text("changed\n")
        head = self.commit()
        self.assertTrue(upstream.scan(self.hub, now=self.now)["review_required"])
        (self.hub / "docs").mkdir()
        (self.hub / "docs/upstream-reviews.md").write_text(f"- Reviewed through: `{head}`.\n")
        result = upstream.scan(self.hub, now=self.now + timedelta(hours=1))
        self.assertFalse(result["review_required"])
        self.assertEqual((self.hub / "upstream.json").read_text(), self.provenance)

    def test_unrelated_plugin_changes_do_not_trigger_review(self):
        (self.source / "other-plugin.md").write_text("unrelated\n")
        self.commit()
        result = upstream.scan(self.hub, now=self.now)
        self.assertFalse(result["review_required"])
        self.assertEqual(result["changes"], [])

    def test_concurrent_check_does_not_remove_another_lock(self):
        lock = self.hub / ".kw-state/upstream/checking.lock"
        lock.mkdir(parents=True)
        self.assertEqual(upstream.scan(self.hub, now=self.now)["status"], "busy")
        self.assertTrue(lock.is_dir())


if __name__ == "__main__":
    unittest.main()
