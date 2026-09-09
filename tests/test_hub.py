import contextlib
import importlib.util
import io
from pathlib import Path
import shutil
import tempfile
import unittest


ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location("kw_hub", ROOT / "bin/kw.py")
hub = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(hub)


class HubTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.home = Path(self.tmp.name) / "home"
        self.output = contextlib.redirect_stdout(io.StringIO())
        self.output.__enter__()
        self.addCleanup(self.output.__exit__, None, None, None)

    def test_preview_creates_nothing(self):
        hub.change_links(hub.link_plan(ROOT, self.home))
        self.assertFalse(self.home.exists())

    def test_install_reread_repeat_and_remove(self):
        hub.change_links(hub.link_plan(ROOT, self.home), apply=True)
        for runtime_path in (".claude/skills", ".agents/skills"):
            path = self.home / runtime_path / "kw-mode"
            self.assertTrue(path.is_symlink())
            self.assertEqual((path / "SKILL.md").read_bytes(), (ROOT / "skills/kw-mode/SKILL.md").read_bytes())
        self.assertEqual(hub.doctor(ROOT, self.home, installed=True), 0)
        hub.change_links(hub.link_plan(ROOT, self.home), apply=True)
        hub.change_links(hub.link_plan(ROOT, self.home), apply=True, remove=True)
        self.assertFalse((self.home / ".claude/skills/kw-mode").is_symlink())
        self.assertFalse((self.home / ".agents/skills/kw-mode").is_symlink())
        self.assertTrue((ROOT / "skills/kw-mode/SKILL.md").is_file())

    def test_conflict_prevents_all_installation(self):
        existing = self.home / ".agents/skills/kw-mode"
        existing.mkdir(parents=True)
        (existing / "mine.txt").write_text("preserve this")
        with self.assertRaises(ValueError):
            hub.change_links(hub.link_plan(ROOT, self.home), apply=True)
        self.assertFalse((self.home / ".claude/skills").exists())
        self.assertEqual((existing / "mine.txt").read_text(), "preserve this")

    def test_foreign_broken_symlink_is_preserved(self):
        existing = self.home / ".claude/skills/kw-mode"
        existing.parent.mkdir(parents=True)
        existing.symlink_to(self.home / "missing")
        with self.assertRaises(ValueError):
            hub.change_links(hub.link_plan(ROOT, self.home), apply=True, remove=True)
        self.assertEqual(existing.readlink(), self.home / "missing")

    def test_shared_skill_directory_is_deduplicated(self):
        shared = self.home / "shared"
        shared.mkdir(parents=True)
        for parent in (".claude", ".agents"):
            (self.home / parent).mkdir()
            (self.home / parent / "skills").symlink_to(shared, target_is_directory=True)
        plan = hub.link_plan(ROOT, self.home)
        self.assertEqual(len(plan), 1)
        hub.change_links(plan, apply=True)
        self.assertEqual(hub.doctor(ROOT, self.home, installed=True), 0)

    def test_single_runtime_install(self):
        hub.change_links(hub.link_plan(ROOT, self.home, ["claude"]), apply=True)
        self.assertTrue((self.home / ".claude/skills/kw-mode").is_symlink())
        self.assertFalse((self.home / ".agents").exists())

    def test_doctor_detects_broken_reference(self):
        repo = Path(self.tmp.name) / "repo"
        shutil.copytree(ROOT, repo, ignore=shutil.ignore_patterns("__pycache__", ".git"))
        (repo / "skills/kw-mode/workflows/verify.md").unlink()
        self.assertEqual(hub.doctor(repo), 1)

    def test_doctor_detects_unreachable_reference(self):
        repo = Path(self.tmp.name) / "repo"
        shutil.copytree(ROOT, repo, ignore=shutil.ignore_patterns("__pycache__", ".git"))
        (repo / "skills/kw-mode/lost.md").write_text("# Lost\n")
        self.assertEqual(hub.doctor(repo), 1)

    def test_containment_rejects_escape(self):
        with self.assertRaises(ValueError):
            hub.inside(ROOT, "../outside")


if __name__ == "__main__":
    unittest.main()
