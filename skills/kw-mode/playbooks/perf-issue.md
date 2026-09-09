# Performance

1. Define the metric, workload, environment, and reproducible baseline. Capture a
   profile on the actual slow surface before choosing an optimization.
2. Ground the trace with [how](../workflows/how.md). Distinguish required work from
   removable work. Consider elimination, partitioning, caching, batching, lazy
   evaluation, or scheduling only when the trace supports that mechanism.
3. State one hypothesis and implement the smallest experiment. Use
   [architect](../workflows/architect.md) for a structural change.
4. Repeat the same workload and compare artifacts. Account for noise, cold/warm
   state, and regressions in other dimensions. Inconclusive is not an improvement.
5. Keep measured improvements, remove unsuccessful task-owned experiments, and
   run [verify](../workflows/verify.md) for behavior as well as speed.
6. Complete authorized delivery through [opening a PR](opening-a-pr.md).

Reply with baseline, result, units, conditions, delta, and artifact paths. Sustained
optimization toward a target uses [hillclimb](hillclimb.md).
