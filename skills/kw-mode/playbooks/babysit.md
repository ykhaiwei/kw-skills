# Babysit

1. Resolve the repository, forge, exact PR/MR scope, and current head/base revisions.
   Read review threads, checks, conflicts, and the requested terminal condition.
   Declare the scope before polling: `check` is one read-only status pass, `drive`
   continues to merge-ready, and `threads-only` addresses the requested review
   threads. A status question ends after its report; it does not start repairs.
2. Classify each blocker as a defect, review decision, conflict, flaky check, or
   external dependency. Inspect evidence before rerunning checks or changing code.
   A suspected flake or infrastructure fault gets one fresh CI run. If the same
   failure recurs, inspect its logs and revise the diagnosis before further action;
   do not repeatedly retry unchanged failures.
3. Fix authorized issues in isolated work. Address the underlying cause, preserve
   intent, and [verify](../workflows/verify.md) each changed artifact.
4. Refresh review and CI state after changes. An old passing check or review does
   not certify a new head. Respond externally only within the granted scope.
5. Continue until the requested reviews are merge-ready or a concrete blocker
   remains. Use native waiting where available and preserve a handoff if the
   session cannot continue.
6. Report current links, heads, checks, review disposition, and blockers. Merge-ready
   is the endpoint unless landing was requested; then use [shipping](shipping.md).
