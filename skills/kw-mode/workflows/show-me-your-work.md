# Show your work

For a long run or an explicit audit request, keep a decision log at a task-owned
path. Use the project's artifact convention, otherwise a scratch directory and
report its path. Commit evidence only when appropriate to the task and authorized.

Use a small TSV with fields `time`, `unit`, `hypothesis`, `action`, `evidence`,
`result`, and `next`. Add a row after each meaningful experiment or decision.
Record rejected attempts as well as accepted changes. Keep secrets and raw private
messages out of the log. Link large measurements rather than inlining them.

Keep the log append-only; correct a false claim with a superseding row and evidence.
When resuming it, identify the current run and the prior rows it inherits. Audit
claims against the actual evidence before handoff without relabeling another
run's observations as your own. Give concurrent writers separate logs to reconcile.

The log supports review and resumption; it does not replace the final explanation.
