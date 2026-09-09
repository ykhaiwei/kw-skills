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


def inside(root, value):
    path = Path(value)
    if path.is_absolute() or ".." in path.parts:
        raise ValueError(f"Expected a relative contained path: {value}")
    resolved = (root / path).resolve()
    if not resolved.is_relative_to(root.resolve()):
        raise ValueError(f"Path escapes repository: {value}")
    return resolved


def registry(root):
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
        if not (skill / "SKILL.md").is_file():
            raise ValueError(f"Missing skill: {name}")
        if not entry.get("runtimes") or any(
            runtime not in data["runtimes"] for runtime in entry["runtimes"]
        ):
            raise ValueError(f"Unknown or empty runtimes for {name}")
    return data


def link_plan(root, home, selected=None):
    data = registry(root)
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


def markdown_targets(path):
    text = path.read_text()
    for target in re.findall(r"\[[^\]]*\]\(([^)]+)\)", text):
        target = target.split("#", 1)[0]
        if not target or re.match(r"[a-zA-Z][a-zA-Z0-9+.-]*:", target):
            continue
        yield (path.parent / target).resolve()


def doctor(root, home=None, installed=False, selected=None):
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
        if not re.search(r"^description: \S.+$", front, re.M):
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
        if not re.fullmatch(r"[a-f0-9]{64}", entry.get("upstream_sha256", "")):
            errors.append(f"Missing source hash: {entry['local']}")
    adapted = set()
    for entry in data["skills"].values():
        skill = inside(root, entry["path"])
        for section in ("principles", "playbooks", "workflows"):
            adapted.update(p.resolve() for p in (skill / section).glob("*.md") if p.name != "index.md")
    if adapted != recorded:
        errors.append("Adapted references and provenance records disagree")
    if not (root / "LICENSE").is_file():
        errors.append("Missing license")
    if installed:
        for runtime, _, destination, status in link_plan(root, home or Path.home(), selected):
            if status != "linked":
                errors.append(f"{runtime}: {status} at {destination}")
    if errors:
        for error in errors:
            print(f"FAIL {error}")
        return 1
    count = sum(1 for entry in data["skills"].values() for _ in inside(root, entry["path"]).rglob("*.md"))
    print(f"PASS {len(registered)} skill, {count} markdown files, references and provenance valid")
    if installed:
        print("PASS selected runtime symlinks resolve to this source")
    return 0


def main(argv=None):
    args_list = sys.argv[1:] if argv is None else argv
    alias = Path(sys.argv[0]).name
    if alias in {"link", "doctor", "test"}:
        args_list = [alias, *args_list]
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest="command", required=True)
    link = sub.add_parser("link", help="Preview or apply skill symlinks")
    link.add_argument("--apply", action="store_true")
    link.add_argument("--remove", action="store_true")
    check = sub.add_parser("doctor", help="Validate references, provenance, and optional installation")
    check.add_argument("--installed", action="store_true")
    for command in (link, check):
        command.add_argument("--home", type=Path, default=Path.home(), help="Override installation home for testing")
        command.add_argument("--runtime", action="append", choices=["claude", "codex"])
    sub.add_parser("test", help="Run installer and integrity tests")
    args = parser.parse_args(args_list)
    try:
        if args.command == "doctor":
            return doctor(ROOT, args.home, args.installed, args.runtime)
        if args.command == "link":
            if doctor(ROOT):
                return 1
            plan = link_plan(ROOT, args.home.expanduser().resolve(), args.runtime)
            change_links(plan, args.apply, args.remove)
            return 0
        return subprocess.call([sys.executable, "-m", "unittest", "discover", "-s", str(ROOT / "tests"), "-v"], cwd=ROOT)
    except (OSError, ValueError, KeyError, TypeError) as error:
        print(f"ERROR {error}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    sys.exit(main())
