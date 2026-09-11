# Upstream review log

Ask your agent: **“Check pstack for useful updates to kw mode.”**

The [review playbook](../skills/kw-mode/playbooks/upstream-review.md) compares new
upstream changes, checks whether they suit kw mode, and records recommendations
here. kw mode automatically runs a due check at the first substantive task in a
session, fetching upstream at most weekly after successful checks. It reviews
new candidates when practical without holding up the main task. No process runs
between sessions, and imports are separate. “Check and apply the worthwhile
updates” also authorizes local adoption. A request to check alone leaves the
engineering instructions unchanged.

This log records what has been reviewed. [upstream.json](../upstream.json) records
the sources actually imported. Keep both when moving computers so deferred ideas
and the next comparison baseline survive.

## Latest completed review

- Reviewed on: 2026-09-11 (UTC).
- Compared from: `27e2a62ff94f9af4b5e68435e41cdceacadb840c`.
- Reviewed through: `f5bdd6826fd0a0d9cbc4347134c3a74a200b9d9d`.
- Observed pstack version: `0.15.2`.
- Coverage: all five changed files under `pstack/`; two commits. No added,
  renamed, or deleted files in this comparison.
- Next suggested check: 2026-09-18. An explicit prompt can check sooner.
- Imported changes from this review: none.

## Decisions and pending ideas

| Upstream change | Decision | Reason and local target |
| --- | --- | --- |
| Evidence and uncertainty wording in the mode entrypoint ([source commit](https://github.com/cursor/plugins/commit/f8abeddd1862dc73704e3d719dd73df0d51b8c71)) | Adapt; pending | Make the distinction between observed results, inference, and speculation explicit in `skills/kw-mode/workflows/writing.md`. kw already asks for evidence, but this would clarify how to state uncertainty. Avoid requiring a mechanical label on every sentence. |
| Neutral operator pronouns in the mode entrypoint and the three changed playbooks ([source commit](https://github.com/cursor/plugins/commit/f5bdd6826fd0a0d9cbc4347134c3a74a200b9d9d)) | Skip | kw's corresponding entrypoint, `autopilot-full.md`, `autopilot-stack.md`, and `multi-phase-plan.md` already use neutral wording. |
| In-chat status wording in upstream `multi-phase-plan.md` (same source commit) | Skip | kw's plan playbook has no copied status-tick mechanism. Its runtime contract already uses native session tools. No corresponding defect was found in the local file. |
| Cursor plugin manifest version change | Skip | kw has its own shared skill setup. A review does not advance the imported pstack version. |

For the next review, retain pending ideas until adopted or explicitly declined.
Append a dated review with source links and decisions, then update the completed
checkpoint above. If a check fails or only part of the diff was reviewed, record
that separately without advancing the checkpoint.
