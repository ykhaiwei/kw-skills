#!/usr/bin/env python3
"""Check for upstream changes at most weekly; never import or execute them."""

import argparse
from datetime import datetime, timedelta, timezone
import json
from pathlib import Path
import re
import subprocess
import tempfile


HUB = Path(__file__).resolve().parents[3]


def git(directory, *args):
    return subprocess.run(
        ["git", "-C", str(directory), *args], check=True, capture_output=True,
        timeout=60,
    ).stdout.decode("utf-8")


def read_json(path):
    return json.loads(path.read_text()) if path.exists() else {}


def save_json(path, value):
    temporary = path.with_suffix(".tmp")
    temporary.write_text(json.dumps(value, indent=2) + "\n")
    temporary.replace(path)


def reviewed_commit(hub, provenance):
    log = hub / "docs/upstream-reviews.md"
    match = re.search(r"^- Reviewed through: `([a-f0-9]{40})`", log.read_text(), re.M) if log.exists() else None
    return match[1] if match else provenance["commit"]


def scan(hub=HUB, force=False, now=None):
    now = now or datetime.now(timezone.utc)
    provenance = read_json(hub / "upstream.json")
    baseline = reviewed_commit(hub, provenance)
    repository = provenance["repository"]
    if not re.fullmatch(r"[a-f0-9]{40}", baseline):
        raise ValueError("Review baseline must be a full commit ID")
    cache = hub / ".kw-state/upstream"
    cache.mkdir(parents=True, exist_ok=True)
    lock = cache / "checking.lock"
    try:
        lock.mkdir()
    except FileExistsError:
        return {"status": "busy", "message": "Another check holds the lock; continue the task.", "lock": str(lock)}
    try:
        previous = read_json(cache / "state.json")
        failure = read_json(cache / "failure.json")
        if not force and failure and now < datetime.fromisoformat(failure["retry_after"]):
            return {"status": "retry_later", **failure}
        if (not force and previous.get("repository") == repository
                and now < datetime.fromisoformat(previous["checked_at"]) + timedelta(days=7)):
            report = {**previous, "status": "fresh"}
            # A reviewed checkpoint consumes the report; no repeated review prompt.
            if baseline == previous["head"]:
                report["review_required"] = False
            elif baseline != previous["baseline"]:
                # Another computer may have supplied a newer review checkpoint.
                report["review_required"] = False
                report["message"] = "Review checkpoint changed; next due check will compare from it."
            return report
        with tempfile.TemporaryDirectory(prefix="kw-upstream-") as temporary:
            checkout = Path(temporary) / "source"
            git(Path(temporary), "clone", "--filter=blob:none", "--no-checkout",
                "--single-branch", "--branch", "main", "--", repository, str(checkout))
            head = git(checkout, "rev-parse", "HEAD").strip()
            try:
                git(checkout, "cat-file", "-e", baseline + "^{commit}")
            except subprocess.CalledProcessError:
                git(checkout, "fetch", "origin", baseline)
            changes = git(checkout, "diff", "--name-status", "--find-renames", baseline, head, "--", "pstack")
            commits = git(checkout, "log", "--oneline", baseline + ".." + head, "--", "pstack")
            diff = git(checkout, "diff", "--no-ext-diff", "--no-textconv", baseline, head, "--", "pstack")
            version = json.loads(git(checkout, "show", head + ":pstack/.cursor-plugin/plugin.json"))["version"]
            report = {
                "status": "checked", "checked_at": now.isoformat(),
                "repository": repository, "baseline": baseline, "head": head,
                "version": version, "review_required": bool(changes),
                "changes": changes.splitlines(), "commits": commits.splitlines(),
                "diff_path": str(cache / "latest.diff"),
            }
            diff_temp = cache / "latest.diff.tmp"
            diff_temp.write_bytes(diff.encode("utf-8"))
            diff_temp.replace(cache / "latest.diff")
            save_json(cache / "state.json", report)
            (cache / "failure.json").unlink(missing_ok=True)
            return report
    except (OSError, ValueError, KeyError, subprocess.SubprocessError) as error:
        failure = {"attempted_at": now.isoformat(),
                   "retry_after": (now + timedelta(days=1)).isoformat(),
                   "error": str(error)}
        save_json(cache / "failure.json", failure)
        return {"status": "error", **failure}
    finally:
        lock.rmdir()


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--force", action="store_true", help="Check now, ignoring the weekly interval and failure cooldown")
    args = parser.parse_args()
    try:
        report = scan(force=args.force)
    except (OSError, ValueError, KeyError) as error:
        report = {"status": "error", "error": str(error)}
    print(json.dumps(report, indent=2))
    return 1 if report["status"] == "error" else 0


if __name__ == "__main__":
    raise SystemExit(main())
