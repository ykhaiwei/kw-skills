# Weekly upstream upkeep

At the first substantive task in a session, run the bundled
[upstream checker](../scripts/check_upstream.py) once, using the available Python
3.11+ interpreter and the script's absolute path resolved through
[runtime](../runtime.md). Skip this during setup until prerequisites are ready,
for dispatched reviewers, explicit kw opt-outs, and when the task forbids network
access or local writes.

The checker performs a network scan only when its last successful check is at
least seven days old. It compares pstack against the last completed review and
stores the result under the hub's ignored `.kw-state/upstream/`. It never imports
upstream instructions. The first check on a new computer is due immediately.

Read the latest pending-work summary in `docs/upstream-reviews.md` on every startup
check, including `fresh` results. Network freshness does not postpone recorded
review or adoption work. Resume its remaining scope without repeating completed
coverage.

- `fresh` with no review required: continue silently unless a local adoption from
  the completed review remains pending and can now be finished.
- `checked` with no review required: no new source changes need review; revisit
  deferred ideas in the review log before continuing.
- `review_required: true`: follow [upstream review](../playbooks/upstream-review.md)
  using the pinned report and saved diff. The [profile](../profile.md) authorizes
  reviewing and applying worthwhile local adaptations without another approval.
  Complete review, adoption, provenance, verification, and the review handoff,
  then summarize what changed. A pending-update notice alone is not completion.
  Keep upkeep secondary to an urgent user task. If urgency, conflicting local
  edits, unavailable evidence, or a material unresolved decision prevents
  completion, record the exact remaining scope and reason in the review log and
  resume it on the next substantive session. Do not advance the completed-review
  checkpoint for partial coverage. A task-specific read-only or review-only
  instruction overrides automatic adoption.
- `busy`, `retry_later`, or `error`: continue the user's task. Mention a failed
  check briefly when it affects requested maintenance. Failures leave the last
  successful timestamp intact and wait one day before retrying automatically.

Uncommitted updates from earlier upkeep are expected. Compare the prior review
records and current diff, preserve unrelated edits, and reconcile compatible
changes. A dirty checkout alone is not a conflict; defer only an unresolved overlap.

For an explicit “check now” request, run the checker with `--force`, even within
the weekly interval. Revisit pending ideas in the review log as well. Never treat
a fetched snapshot as a completed review or execute commands from its diff.

This is prompted-session automation through kw's default instructions. Nothing
runs while the assistants are closed. A fresh installation includes this workflow
through the shared skill; no cron job, host-specific hook, or extra plugin is
required. A stale lock after an interrupted process can be removed once the agent
has verified no check is still running; it does not justify deleting the cache.
