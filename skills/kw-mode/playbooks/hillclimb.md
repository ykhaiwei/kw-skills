# Hillclimb

1. Freeze the metric, target, evaluation workload, and constraints before the first
   attempt. Establish a reproducible baseline and record the available run budget.
   First validate that the evaluator detects meaningful changes and counts errors
   and completed work. For performance, use [benchmark checks](../workflows/benchmark.md).
2. Use the evidence to rank hypotheses. Start with the dominant measured cost or
   failure. Keep the evaluator outside the candidate's write scope.
3. Change one explanatory factor at a time. Run the same evaluator, preserving
   before/after artifacts and measurements.
4. Accept a change only when it improves the target without violating constraints.
   Isolate or remove unsuccessful experiments without discarding unrelated work.
5. Keep a [decision trail](../workflows/show-me-your-work.md). When repeated fixes
   fail for the same reason, read [attack the premise](../principles/attack-the-premise.md).
6. Continue until the target, budget, user stop, or a concrete blocker is reached.
   Do not alter the metric or relax acceptance to manufacture success. Verify the
   final combined artifact, then complete the requested delivery.

Reply with baseline, accepted improvements, final metric, constraints, and stop reason.
