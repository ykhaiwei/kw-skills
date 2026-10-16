# Make Operations Idempotent

Design repeatable operations to converge on the intended state after retries and partial failures. Derive each step from what exists now, compare it with the goal, and apply the remaining difference.

Anything a run leaves behind, such as a lock, temporary file, partial record, or claimed job, needs enough evidence for a later run to distinguish live work from abandoned state. A PID alone may be reused or refer to another host; use ownership and liveness evidence appropriate to the system. Do not discard state whose ownership is unresolved.

Use atomic replacement where appropriate, recognize already-completed work by stable identity or content, and reconcile partial results. Idempotence does not itself prevent concurrent writers: use the ownership or synchronization required by the actual shared resource.

Check three cases:

1. The operation runs twice in a row.
2. A prior run stops at each meaningful mutation boundary.
3. Re-execution converges without duplicating effects or damaging live work.

If a retry depends on an uncheckable assumption about the previous run, improve the state representation or reconciliation step.
