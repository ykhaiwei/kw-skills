# Review upstream updates

Use for “check pstack for useful updates”, “weekly KW update check”, or a request
to refresh this mode from upstream. [Weekly upkeep](../workflows/weekly-upkeep.md)
also routes here when its automatic scan discovers changes. Use its saved report
and diff when available; an explicit check-now request first forces a fresh scan.

1. Resolve the hub root through [runtime](../runtime.md). Read its `upstream.json`,
   `docs/upstream-reviews.md`, and the local [profile](../profile.md). Keep the
   imported source baseline separate from the latest completed review. A check
   reports recommendations and updates the review log; importing changes requires
   an update request. An explicit read-only request leaves even the log unchanged.
2. Reuse the checker's pinned snapshot report and full diff when available. Fetch
   the recorded repository into a task-owned temporary checkout if additional
   source context is needed, or if checking manually without that report. Inspect
   `pstack/` as source material; do not execute its setup, hooks, or workflows.
   Pin the current `main` commit before reading files so the review uses one
   snapshot. If the network is unavailable, report that the check is incomplete
   and leave the completed-review checkpoint unchanged.
3. Compare the last fully reviewed commit with that snapshot, or use the
   `upstream.json` commit for the first review. Read the path-scoped commit log,
   changed-file inventory, and full relevant diffs. Include added, renamed, and
   deleted files, including unmapped skills; checking only imported files misses
   new ideas. If the old commit is unavailable, try fetching it; do not substitute
   another baseline silently. If history diverged, disclose it and compare the
   endpoint trees. Revisit pending recommendations even when there are no new
   upstream changes.
4. Judge each change against KW's actual files and recorded adaptations. Recommend
   **adopt**, **adapt**, **skip**, or **defer**, with a concrete benefit, local
   target, and source commit/file. Favor changes that improve investigation,
   design, verification, or clarity. Preserve Claude-first native operation,
   inherited models, user scope, and local preferences. Cursor-only mechanisms
   need a useful native equivalent before import. Do not replace an entire local
   file merely because upstream changed it.
5. Write the outcome to the hub's `docs/upstream-reviews.md`: UTC review date,
   compared commits, version observed, scope covered, decisions, and unresolved
   candidates. Advance its completed checkpoint only after every changed item
   has a disposition. Keep deferred items visible at future checks. For a partial
   review, record coverage without advancing the checkpoint. A completed check
   with identical trees can advance it and report no new changes. Set the next
   suggested check seven days later; an explicit check-now request still fetches
   fresh evidence sooner. Finish with the few recommendations worth discussing.
6. When the request includes adoption, implement the selected changes through
   [authoring a skill](authoring-a-skill.md). Verify and record their disposition.
   Update affected provenance entries with the actual source commit, SHA-256 of
   the original source bytes, and adaptation notes. A selective import uses an
   entry-level `upstream_commit`; preserve the top-level baseline for untouched
   entries. Do not relabel all files as the newest version after a partial import.
   Run the hub's doctor and tests. Commit or publish only within the user's scope.

## Comparison recipe

The following is a shell recipe for macOS, Linux, or WSL. Resolve the baseline
from the review log instead of copying an old commit out of a previous chat.
Use equivalent native commands on Windows.

```sh
kw_upstream_dir=$(mktemp -d)
git clone --filter=blob:none --no-checkout https://github.com/cursor/plugins.git "$kw_upstream_dir/plugins"
git -C "$kw_upstream_dir/plugins" rev-parse HEAD
```

Use the resulting checkout for the commands below. Substitute the resolved
commit IDs for `BASE` and `HEAD_SHA` before running them:

```sh
git log --oneline BASE..HEAD_SHA -- pstack
git diff --name-status --find-renames BASE HEAD_SHA -- pstack
git diff BASE HEAD_SHA -- pstack
git show HEAD_SHA:pstack/.cursor-plugin/plugin.json
```

Use `git show COMMIT:path` to read old and new source, and map those paths through
the hub's `upstream.json` to the adapted local files. Split large diffs by file so
truncated output cannot be mistaken for complete coverage. A changed version is
a discovery hint; the actual diff determines whether there is anything to adopt.
