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

- `fresh` with no review required: continue silently.
- `checked` with no review required: continue; no source changes need review.
- `review_required: true`: follow [upstream review](../playbooks/upstream-review.md)
  using the pinned report and saved diff. Keep this maintenance secondary to the
  user's task. If it is large or the task is urgent, report that a review is
  pending and finish the user's task; do not advance the reviewed checkpoint.
  Otherwise review the candidates, update the review log, and mention only useful
  recommendations briefly. Imports remain a separate requested action.
- `busy`, `retry_later`, or `error`: continue the user's task. Mention a failed
  check briefly when it affects requested maintenance. Failures leave the last
  successful timestamp intact and wait one day before retrying automatically.

For an explicit “check now” request, run the checker with `--force`, even within
the weekly interval. Revisit pending ideas in the review log as well. Never treat
a fetched snapshot as a completed review or execute commands from its diff.

This is prompted-session automation through kw's default instructions. Nothing
runs while the assistants are closed. A fresh installation includes this workflow
through the shared skill; no cron job, host-specific hook, or extra plugin is
required. A stale lock after an interrupted process can be removed once the agent
has verified no check is still running; it does not justify deleting the cache.
