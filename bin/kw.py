#!/usr/bin/env python3
"""Validate the KW hub and manage only its registered skill symlinks."""

import argparse
import json
import os
from pathlib import Path
import re
import subprocess
import sys
import tomllib


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_START = "\n<!-- kw-mode:begin -->\n"
DEFAULT_END = "<!-- kw-mode:end -->\n"


def inside(root, value):
    path = Path(value)
    if path.is_absolute() or ".." in path.parts:
        raise ValueError(f"Expected a relative contained path: {value}")
    resolved = (root / path).resolve()
    if not resolved.is_relative_to(root.resolve()):
        raise ValueError(f"Path escapes repository: {value}")
    return resolved


def registry(root, require_sources=True):
    data = tomllib.loads((root / "registry.toml").read_text())
    if data.get("meta", {}).get("version") != 1:
        raise ValueError("Unsupported registry version")
    if not data.get("skills") or not data.get("runtimes"):
        raise ValueError("Registry needs skills and runtimes")
    for runtime, entry in data["runtimes"].items():
        path = Path(entry["skills_dir"])
        if path.is_absolute() or ".." in path.parts or len(path.parts) < 2:
            raise ValueError(f"Invalid skills directory for {runtime}")
    for name, entry in data["skills"].items():
        if not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", name):
            raise ValueError(f"Invalid skill name: {name}")
        skill = inside(root, entry["path"])
        if require_sources and not (skill / "SKILL.md").is_file():
            raise ValueError(f"Missing skill: {name}")
        if not entry.get("runtimes") or any(
            runtime not in data["runtimes"] for runtime in entry["runtimes"]
        ):
            raise ValueError(f"Unknown or empty runtimes for {name}")
    return data


def link_plan(root, home, selected=None, remove=False):
    data = registry(root, require_sources=not remove)
    selected = set(selected or data["runtimes"])
    if selected - data["runtimes"].keys():
        raise ValueError("Unknown runtime selection")
    result = []
    destinations = {}
    for name, entry in data["skills"].items():
        source = inside(root, entry["path"])
        for runtime in entry["runtimes"]:
            if runtime not in selected:
                continue
            logical = home / data["runtimes"][runtime]["skills_dir"] / name
            destination = logical.parent.resolve() / logical.name
            if destination in destinations:
                if destinations[destination] != source:
                    raise ValueError(f"Conflicting registry targets: {destination}")
                continue
            destinations[destination] = source
            if destination.is_symlink() and destination.resolve() == source:
                status = "linked"
            elif os.path.lexists(destination):
                status = "conflict"
            else:
                status = "missing"
            result.append((runtime, source, destination, status))
    return result


def change_links(plan, apply=False, remove=False):
    conflicts = [str(dest) for _, _, dest, status in plan if status == "conflict"]
    if conflicts:
        raise ValueError("Existing paths left untouched: " + ", ".join(conflicts))
    created = []
    try:
        for runtime, source, destination, status in plan:
            action = ("remove" if status == "linked" else "absent") if remove else (
                "keep" if status == "linked" else "link"
            )
            print(f"{action:6} {runtime:6} {destination} -> {source}")
            if not apply:
                continue
            if action == "link":
                destination.parent.mkdir(parents=True, exist_ok=True)
                destination.symlink_to(source, target_is_directory=True)
                created.append(destination)
            elif action == "remove":
                if not destination.is_symlink() or destination.resolve() != source:
                    raise ValueError(f"Link changed during removal: {destination}")
                destination.unlink()
    except Exception:
        for destination in reversed(created):
            if destination.is_symlink():
                destination.unlink()
        raise
    if not apply:
        print("Preview only. Add --apply to make these changes.")


def default_text(before, block):
    if "<!-- kw-mode:begin -->" in before or "<!-- kw-mode:end -->" in before:
        if before.count(DEFAULT_START) != 1 or before.count(DEFAULT_END) != 1:
            raise ValueError("Malformed KW default block; existing instructions left untouched")
        start = before.index(DEFAULT_START)
        end = before.index(DEFAULT_END)
        if end < start:
            raise ValueError("Reversed KW default markers; existing instructions left untouched")
        return before[:start] + block + before[end + len(DEFAULT_END):]
    return before + block


def default_plan(root, home, selected=None, remove=False):
    data = registry(root, require_sources=not remove)
    selected = set(selected or data["skills"]["kw-mode"]["runtimes"])
    if selected - data["runtimes"].keys():
        raise ValueError("Unknown runtime selection")
    skill_file = inside(root, data["skills"]["kw-mode"]["path"]) / "SKILL.md"
    block = ""
    if not remove:
        template = (root / "instructions/default.md").read_text()
        block = DEFAULT_START + template.format(skill_file=skill_file, hub_root=root.resolve()).strip() + "\n" + DEFAULT_END
    destinations = []
    if "claude" in selected:
        destinations.append(("claude", home / ".claude/CLAUDE.md"))
    if "codex" in selected:
        codex_dir = home / ".codex"
        if home.resolve() == Path.home().resolve() and os.environ.get("CODEX_HOME"):
            codex_dir = Path(os.environ["CODEX_HOME"]).expanduser()
        override = codex_dir / "AGENTS.override.md"
        normal = codex_dir / "AGENTS.md"
        if remove:
            destinations.extend(("codex", path) for path in (normal, override))
        else:
            active = override if override.is_file() and override.read_text().strip() else normal
            destinations.append(("codex", active))
    result = []
    seen = set()
    for runtime, destination in destinations:
        destination = destination.resolve()
        if destination in seen:
            continue
        seen.add(destination)
        before = destination.read_bytes().decode() if destination.exists() else ""
        after = default_text(before, block)
        result.append((runtime, destination, before, after))
    return result


def change_defaults(plan, apply=False):
    for runtime, destination, before, after in plan:
        action = "keep" if before == after else "update"
        print(f"{action:6} {runtime:6} default instructions: {destination}")
        if before == after:
            continue
        if not apply:
            if DEFAULT_START in after:
                start = after.index(DEFAULT_START)
                end = after.index(DEFAULT_END) + len(DEFAULT_END)
                print(after[start:end])
            else:
                print("Remove the KW default block; preserve all surrounding text.")
            continue
        current = destination.read_bytes().decode() if destination.exists() else ""
        if current != before:
            raise ValueError(f"Instructions changed during setup: {destination}")
        destination.parent.mkdir(parents=True, exist_ok=True)
        destination.write_bytes(after.encode())


def markdown_targets(path):
    text = path.read_text()
    for target in re.findall(r"\[[^\]]*\]\(([^)]+)\)", text):
        target = target.split("#", 1)[0]
        if not target or re.match(r"[a-zA-Z][a-zA-Z0-9+.-]*:", target):
            continue
        yield (path.parent / target).resolve()


def has_description(front):
    """Check presence in common scalar forms, not the complete YAML grammar."""
    lines = front.splitlines()
    for index, line in enumerate(lines):
        if not line.startswith("description:"):
            continue
        value = line.partition(":")[2].strip()
        if re.fullmatch(r"[>|][+-]?(?:[ \t]+#.*)?", value):
            for following in lines[index + 1:]:
                if following.strip():
                    return following.startswith((" ", "\t"))
            return False
        if value.startswith(('"', "'")):
            return len(value) > 1 and value[-1] == value[0] and bool(value[1:-1].strip())
        return bool(value) and not value.startswith("#")
    return False


def doctor(root, home=None, installed=False, selected=None, quiet=False, defaults=False):
    root = root.resolve()
    data = registry(root)
    errors = []
    all_skills = {p.parent.resolve() for p in (root / "skills").rglob("SKILL.md")}
    registered = {inside(root, e["path"]) for e in data["skills"].values()}
    if all_skills != registered:
        errors.append("Skill folders and registry disagree")
    for name, entry in data["skills"].items():
        skill = inside(root, entry["path"])
        text = (skill / "SKILL.md").read_text()
        parts = text.split("---", 2)
        if len(parts) != 3 or parts[0].strip():
            errors.append(f"Missing frontmatter: {name}")
            continue
        front = parts[1]
        if not re.search(rf"^name: {re.escape(name)}$", front, re.M):
            errors.append(f"Frontmatter name mismatch: {name}")
        if not has_description(front):
            errors.append(f"Missing description: {name}")
        pending = [skill / "SKILL.md"]
        reached = set()
        while pending:
            path = pending.pop().resolve()
            if path in reached:
                continue
            reached.add(path)
            for target in markdown_targets(path):
                if not target.is_relative_to(skill):
                    errors.append(f"Reference leaves skill: {path.name} -> {target}")
                elif not target.exists():
                    errors.append(f"Broken reference: {path.name} -> {target.name}")
                elif target.is_file() and target.suffix == ".md":
                    pending.append(target)
        for path in skill.rglob("*.md"):
            if path.resolve() not in reached:
                errors.append(f"Unreachable reference: {path.relative_to(root)}")
            if "[TODO:" in path.read_text():
                errors.append(f"Unfinished scaffold: {path.relative_to(root)}")
    provenance = json.loads((root / "upstream.json").read_text())
    if not re.fullmatch(r"[a-f0-9]{40}", provenance.get("commit", "")):
        errors.append("Upstream commit is not pinned")
    recorded = set()
    for entry in provenance["files"]:
        local = inside(root, entry["local"])
        if not local.is_file() or local in recorded:
            errors.append(f"Missing or duplicate provenance target: {entry['local']}")
        recorded.add(local)
        origin = entry.get("origin", "upstream")
        if origin == "upstream":
            if not entry.get("upstream"):
                errors.append(f"Missing upstream path: {entry['local']}")
            if not re.fullmatch(r"[a-f0-9]{64}", entry.get("upstream_sha256", "")):
                errors.append(f"Missing source hash: {entry['local']}")
        elif origin == "local":
            if "upstream" in entry or "upstream_sha256" in entry:
                errors.append(f"Local entry has upstream fields: {entry['local']}")
        else:
            errors.append(f"Unknown origin {origin!r}: {entry['local']}")
    references = set()
    for entry in data["skills"].values():
        skill = inside(root, entry["path"])
        for section in ("principles", "playbooks", "workflows"):
            references.update(p.resolve() for p in (skill / section).glob("*.md") if p.name != "index.md")
    if references != recorded:
        errors.append("References and provenance records disagree")
    if not (root / "LICENSE").is_file():
        errors.append("Missing license")
    if installed:
        for runtime, _, destination, status in link_plan(root, home or Path.home(), selected):
            if status != "linked":
                errors.append(f"{runtime}: {status} at {destination}")
    if defaults:
        for runtime, destination, before, after in default_plan(root, home or Path.home(), selected):
            if before != after:
                errors.append(f"{runtime}: missing or outdated default instructions at {destination}")
    if errors:
        for error in errors:
            print(f"FAIL {error}")
        return 1
    if not quiet:
        count = sum(1 for entry in data["skills"].values() for _ in inside(root, entry["path"]).rglob("*.md"))
        print(f"PASS {len(registered)} skill, {count} markdown files, references and provenance valid")
        if installed:
            print("PASS selected runtime symlinks resolve to this source")
        if defaults:
            print("PASS selected runtimes have current KW default instructions")
    return 0


def main(argv=None):
    args_list = sys.argv[1:] if argv is None else argv
    alias = Path(sys.argv[0]).name
    if alias in {"link", "setup", "doctor", "test"}:
        args_list = [alias, *args_list]
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest="command", required=True)
    link = sub.add_parser("link", help="Preview or apply skill symlinks")
    setup = sub.add_parser("setup", help="Install skill links and make KW mode the default")
    for command in (link, setup):
        command.add_argument("--apply", action="store_true")
        command.add_argument("--remove", action="store_true")
    check = sub.add_parser("doctor", help="Validate references, provenance, and optional installation")
    check.add_argument("--installed", action="store_true")
    check.add_argument("--defaults", action="store_true")
    for command in (link, setup, check):
        command.add_argument("--home", type=Path, default=Path.home(), help="Override installation home for testing")
        command.add_argument("--runtime", action="append", choices=["claude", "codex"])
    sub.add_parser("test", help="Run installer and integrity tests")
    args = parser.parse_args(args_list)
    try:
        if args.command == "doctor":
            return doctor(ROOT, args.home, args.installed, args.runtime, defaults=args.defaults)
        if args.command in {"link", "setup"}:
            if not args.remove and doctor(ROOT, quiet=True):
                return 1
            plan = link_plan(ROOT, args.home.expanduser().resolve(), args.runtime, remove=args.remove)
            instructions = default_plan(ROOT, args.home.expanduser().resolve(), args.runtime, remove=args.remove) if args.command == "setup" else []
            change_links(plan, args.apply, args.remove)
            change_defaults(instructions, args.apply)
            return 0
        return subprocess.call([sys.executable, "-m", "unittest", "discover", "-s", str(ROOT / "tests"), "-v"], cwd=ROOT)
    except (OSError, ValueError, KeyError, TypeError) as error:
        print(f"ERROR {error}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    sys.exit(main())
