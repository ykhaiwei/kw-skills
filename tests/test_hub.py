import contextlib
import importlib.util
import io
import json
from pathlib import Path
import re
import shutil
import subprocess
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

    def copy_repo(self):
        repo = Path(self.tmp.name) / "repo"
        shutil.copytree(
            ROOT, repo, symlinks=True,
            ignore=shutil.ignore_patterns("__pycache__", ".git", ".idea", "REVIEW.txt"),
        )
        return repo

    def run_cli(self, repo, alias, *args):
        return subprocess.run(
            [str(repo / "bin" / alias), *args], cwd=repo,
            text=True, capture_output=True,
        )

    def test_original_playbook_has_local_provenance(self):
        repo = self.copy_repo()
        playbook = "skills/kw-mode/playbooks/local-workflow.md"
        (repo / playbook).write_text("# Local workflow\n\n1. Check local behavior.\n")
        with (repo / "skills/kw-mode/SKILL.md").open("a") as stream:
            stream.write("\n[Local workflow](playbooks/local-workflow.md)\n")
        self.assertEqual(hub.doctor(repo), 1)
        path = repo / "upstream.json"
        data = json.loads(path.read_text())
        data["files"].append({"local": playbook, "origin": "local"})
        path.write_text(json.dumps(data))
        self.assertEqual(hub.doctor(repo), 0)

    def test_upstream_entries_still_require_source_hash(self):
        repo = self.copy_repo()
        path = repo / "upstream.json"
        data = json.loads(path.read_text())
        del data["files"][0]["upstream_sha256"]
        path.write_text(json.dumps(data))
        self.assertEqual(hub.doctor(repo), 1)

    def test_local_provenance_rejects_upstream_fields_and_unknown_origins(self):
        repo = self.copy_repo()
        path = repo / "upstream.json"
        data = json.loads(path.read_text())
        for origin in ("local", "unknown"):
            with self.subTest(origin=origin):
                data["files"][0]["origin"] = origin
                path.write_text(json.dumps(data))
                self.assertEqual(hub.doctor(repo), 1)

    def test_alias_install_and_uninstall_with_broken_content(self):
        repo = self.copy_repo()
        result = self.run_cli(repo, "link", "--apply", "--home", str(self.home))
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        self.assertNotIn("PASS", result.stdout)
        (repo / "skills/kw-mode/workflows/verify.md").unlink()
        result = self.run_cli(repo, "doctor")
        self.assertEqual(result.returncode, 1)
        (repo / "skills/kw-mode/SKILL.md").unlink()
        result = self.run_cli(repo, "link", "--remove", "--home", str(self.home))
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        self.assertTrue((self.home / ".claude/skills/kw-mode").is_symlink())
        result = self.run_cli(repo, "link", "--remove", "--apply", "--home", str(self.home))
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        self.assertFalse((self.home / ".claude/skills/kw-mode").is_symlink())
        self.assertFalse((self.home / ".agents/skills/kw-mode").is_symlink())
        self.assertTrue((repo / "skills/kw-mode/profile.md").is_file())

    def test_description_scalar_forms(self):
        repo = self.copy_repo()
        skill = repo / "skills/kw-mode/SKILL.md"
        original = skill.read_text()
        for description in ('x', '"A description"', '>\n  A folded description.', '>+\n  A folded description.', '>-\n  A folded description.', '|\n  A literal description.'):
            with self.subTest(description=description):
                skill.write_text(re.sub(r"^description: .+$", "description: " + description, original, flags=re.M))
                self.assertEqual(hub.doctor(repo), 0)
        for description in ('', '""', "''", '>\n  ', '|\n  '):
            with self.subTest(empty_description=description):
                skill.write_text(re.sub(r"^description: .+$", "description: " + description, original, flags=re.M))
                self.assertEqual(hub.doctor(repo), 1)

    def test_setup_preview_does_not_create_home(self):
        repo = self.copy_repo()
        result = self.run_cli(repo, "setup", "--home", str(self.home))
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        self.assertIn(str(repo.resolve() / "skills/kw-mode/SKILL.md"), result.stdout)
        self.assertFalse(self.home.exists())

    def test_setup_preserves_user_text_updates_and_removes_defaults(self):
        repo = self.copy_repo()
        paths = [self.home / ".claude/CLAUDE.md", self.home / ".codex/AGENTS.md"]
        original = "# My instructions\r\nPreserve these preferences.\r\n".encode()
        suffix = b"\n# Later note\nKeep this too.\n"
        for path in paths:
            path.parent.mkdir(parents=True)
            path.write_bytes(original)
        result = self.run_cli(repo, "setup", "--apply", "--home", str(self.home))
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        for path in paths:
            data = path.read_bytes()
            self.assertTrue(data.startswith(original))
            self.assertIn(str(repo.resolve() / "skills/kw-mode/SKILL.md").encode(), data)
            path.write_bytes(data + suffix)
        installed = [path.read_bytes() for path in paths]
        result = self.run_cli(repo, "setup", "--apply", "--home", str(self.home))
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        self.assertEqual([path.read_bytes() for path in paths], installed)
        result = self.run_cli(repo, "doctor", "--installed", "--defaults", "--home", str(self.home))
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        with (repo / "instructions/default.md").open("a") as stream:
            stream.write("\nNew default guidance.\n")
        result = self.run_cli(repo, "doctor", "--defaults", "--home", str(self.home))
        self.assertEqual(result.returncode, 1)
        result = self.run_cli(repo, "setup", "--apply", "--home", str(self.home))
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        for path in paths:
            self.assertIn(b"New default guidance.", path.read_bytes())
            self.assertEqual(path.read_bytes().count(b"<!-- kw-mode:begin -->"), 1)
        (repo / "instructions/default.md").unlink()
        (repo / "skills/kw-mode/SKILL.md").unlink()
        result = self.run_cli(repo, "setup", "--remove", "--apply", "--home", str(self.home))
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        for path in paths:
            self.assertEqual(path.read_bytes(), original + suffix)
        self.assertFalse((self.home / ".claude/skills/kw-mode").is_symlink())
        self.assertFalse((self.home / ".agents/skills/kw-mode").is_symlink())

    def test_setup_uses_active_codex_override(self):
        repo = self.copy_repo()
        normal = self.home / ".codex/AGENTS.md"
        override = self.home / ".codex/AGENTS.override.md"
        normal.parent.mkdir(parents=True)
        normal.write_text("Normal guidance.\n")
        override.write_text("Override guidance.\n")
        result = self.run_cli(repo, "setup", "--apply", "--runtime", "codex", "--home", str(self.home))
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        self.assertEqual(normal.read_text(), "Normal guidance.\n")
        self.assertIn("<!-- kw-mode:begin -->", override.read_text())
        self.assertFalse((self.home / ".claude").exists())
        result = self.run_cli(repo, "doctor", "--defaults", "--runtime", "codex", "--home", str(self.home))
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        result = self.run_cli(repo, "setup", "--remove", "--apply", "--runtime", "codex", "--home", str(self.home))
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        self.assertEqual(override.read_text(), "Override guidance.\n")
        self.assertEqual(normal.read_text(), "Normal guidance.\n")

    def test_malformed_default_block_prevents_setup_changes(self):
        repo = self.copy_repo()
        path = self.home / ".codex/AGENTS.md"
        path.parent.mkdir(parents=True)
        original = "My preferences\n<!-- kw-mode:begin -->\nUnclosed block.\n"
        path.write_text(original)
        result = self.run_cli(repo, "setup", "--apply", "--home", str(self.home))
        self.assertEqual(result.returncode, 1)
        self.assertEqual(path.read_text(), original)
        self.assertFalse((self.home / ".claude").exists())
        self.assertFalse((self.home / ".agents").exists())

    def test_link_only_does_not_enable_global_defaults(self):
        repo = self.copy_repo()
        result = self.run_cli(repo, "link", "--apply", "--home", str(self.home))
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        result = self.run_cli(repo, "doctor", "--defaults", "--home", str(self.home))
        self.assertEqual(result.returncode, 1)
        self.assertFalse((self.home / ".claude/CLAUDE.md").exists())
        self.assertFalse((self.home / ".codex/AGENTS.md").exists())


if __name__ == "__main__":
    unittest.main()
