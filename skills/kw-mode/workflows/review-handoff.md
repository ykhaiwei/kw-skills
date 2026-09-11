# Review handoff

After substantial implementation or cleanup, automatically prepare a compact
handoff, obtain an independent review, validate and fix confirmed in-scope
findings, and prepare a logical commit plan. Do not wait for the user to move each
step along. Keep the original agent responsible for implementation and delivery.
Skip casual discussion, plan-only work, and trivial edits unless requested.

Explicit scope takes precedence: “prepare a handoff only” stops after preparation;
“review only” returns findings without source fixes; an opt-out skips this flow.
Being dispatched as a reviewer never triggers another review or weekly upkeep.

## Prepare

Use the project's existing review-artifact convention when present. Otherwise
create `.kw-review/<task>/review.md` in the project being changed. Choose a unique
task directory so concurrent work cannot overwrite another review. Reuse it for
fixes to the same task. Resolve these paths against the project, not the skill hub.

Keep the directory local. If the project does not already ignore it, add
`/.kw-review/` to this checkout's Git exclude file, resolved with
`git rev-parse --git-path info/exclude`, preserving existing entries. Do not change
another project's shared `.gitignore` for personal review notes. This hub ignores
its own handoff directory in its shared `.gitignore`. If the project is not in
Git, use a task-owned temporary directory and report its path.
Respect a user-requested shared or committed review artifact instead when given.

Record only the context needed to review the result:

- The requested outcome, constraints, and intended behavior.
- Repository and branch, base commit, current HEAD, and relevant changed files.
  Include pending tracked and untracked changes. Record content hashes for the
  files under review so later agents can detect changes after the handoff.
- Checks actually run, results, and meaningful gaps. Separate author-reported
  evidence from observations made by the reviewer.
- Open decisions or risks, followed by empty findings and resolution sections.

Link existing evidence instead of copying logs or transcripts. Keep credentials
and unrelated private context out. Report the file path in the completion reply.

## Dispatch automatically

Prefer the opposite runtime: a Codex author requests a Claude reviewer, and a
Claude author requests a Codex reviewer. Use the strongest available review-capable
model there, resolved from current runtime capabilities, model settings, or
official documentation. Honor any explicit model or budget constraint. This is a
review-specific exception to inheriting the implementation model.

Use the [runtime contract](../runtime.md) to launch a fresh reviewer without the
author's conversation. Give it the task contract, snapshot/diff, relevant project
instructions, and acceptance evidence. It must independently inspect the source,
report findings with evidence, leave source unchanged, and not delegate or launch
this workflow again. Freeze the reviewed files while it works; the author can
prepare commit grouping and messages without editing the snapshot.

If the opposite runtime is missing, unauthenticated, unavailable, or cannot run
with the required restrictions, spawn a fresh native reviewer in the current
runtime, using its strongest available model. Do not install tools, switch
accounts, or weaken permissions just to obtain the preferred reviewer. Record
the fallback and actual reviewer/model; same-runtime independent review is valid.
If no independent agent can run, do a local review and explicitly leave independent
review unavailable. A failed or empty reviewer run is not a clean verdict.

Keep the review brief and feedback in the same task directory. Capture CLI output
there rather than requiring permission to edit the source project. The author
copies the reviewer result into the handoff, preserving its attribution and
limitations. Wait using the host's supported facilities and report progress.

## Reviewer contract

When given the handoff and asked to review, read it and follow [review](review.md).
Inspect the actual code and diff independently; the author's summary is context,
not proof. The author verifies the recorded revision and file hashes before
dispatch and after feedback returns. The reviewer independently checks them when
its tools permit and reports that gap otherwise. A reviewer that detects drift
identifies the new scope before giving a verdict. If the author detects drift
after feedback returns, keep that feedback attached to the old snapshot and
request the focused re-review of the new snapshot within this workflow's limit.
Do not silently attach an old review to newer code.

Return feedback to the author, or write it into the handoff if that is the assigned
output and permitted. Each finding gets a stable ID, priority,
location, concrete impact or trigger, and evidence. Record the reviewer and
reviewed snapshot, checks run, and limitations. “No findings” is valid; do not
invent issues to fill the file. Review changes the feedback only, unless fixes
were also requested. If reviewers run concurrently, give each a separate feedback
file in the task directory and have one owner reconcile them into the handoff.

## Fix and close

After the automatic review, or when asked to “fix the feedback”, reproduce or
validate each finding before editing. Record each disposition under its ID:
fixed, declined with evidence, or
deferred with a reason. Preserve the original finding text. Run relevant checks
and update the file snapshot and author verification evidence.

If changes invalidate the review, request a focused re-review automatically.
Distinguish
author verification from independent verification; the fixing agent cannot mark
its own changes independently approved. Re-review changed behavior and affected
boundaries rather than repeating every check without a reason. Use one initial
review and at most one focused re-review by default. If material findings remain,
report them honestly with current fixes and verification instead of cycling
indefinitely or calling the work approved.

Once confirmed findings are resolved, prepare commit groups and concise
`area: imperative summary` messages. Keep each group coherent and independently
reviewable. The original agent owns this step; do not spawn a commit agent.
Record the plan in the handoff. Create commits only when covered by the user's
request; preparing commits does not authorize committing, pushing, or publishing.

Keep the handoff until the task is accepted. It is local working state, not a
permanent repository document. Remove only this task's notes when the user asks
for cleanup, and never erase unresolved feedback from another task.

## File shape

```markdown
# Review: <task>

Status: ready for review

## Context and scope
<Outcome, constraints, base/HEAD, changed files and content hashes>

## Author verification
<Commands, observed results, gaps>

## Reviewer feedback
<Reviewer, snapshot, findings with IDs, evidence, limitations>

## Resolutions
<Finding ID, disposition, fix and verification, re-review status>
```
