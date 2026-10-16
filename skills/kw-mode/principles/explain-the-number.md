# Explain the Number

Before drawing conclusions from a measured speedup, regression, throughput, latency, or eval score, establish what the number measures and what might distort it.

- For performance, ask what bounds the result and why it is not substantially better. Use a profile or counters captured during a run and relate them to the executing path. Source inspection alone is a hypothesis. If the limiter remains unknown, report that uncertainty rather than presenting a diagnosis.
- Rule out plausible alternatives: errors, skipped work, unintended caching, code that never ran, unequal tuning, measurement overhead, noise, and an improvement too small to affect the complete task.
- Keep the evidence with the claim: workload and environment, run count, spread, observed limiter or remaining uncertainty, and a rerunnable command or linked artifact. Compare equivalent work under comparable conditions.
- For evals, verify that trials completed the intended task and that the claimed difference survives repeat trials. Check other models or scenarios when the claim is meant to generalize to them.
- Reconcile local savings with the whole path. A claimed time saving larger than the original cost of the changed component needs explanation.

Use [benchmark checks](../workflows/benchmark.md) for performance comparisons or the [eval playbook](../playbooks/eval.md) for evals. A user-requested rough estimate can stay lightweight when its limits are explicit. [Prove It Works](prove-it-works.md) establishes that an output is real; this principle establishes what the measured result supports.
