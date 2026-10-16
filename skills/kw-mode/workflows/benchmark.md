# Benchmark checks

Before trusting a performance comparison, write the claim and inspect what the
harness times, counts, and excludes. Use tools available on the actual host.

1. Confirm correct outputs, count errors and retries, and prove the intended work
   completed inside the measured region. Await asynchronous work and consume lazy
   results. Fast failures or unused results are not speedups.
2. Compare equivalent workloads and realistic configurations: builds, versions,
   data, concurrency, batching, indexes, and cache state. For an adoption decision,
   tune each option fairly or report the unresolved comparison.
3. Find the limiting resource or code path using a separate diagnostic run, so
   profiling overhead does not contaminate reported timing. Check machine load
   and whether the load generator saturates before the system being measured.
4. Repeat and interleave baseline and candidate runs to reduce warmup and drift
   bias. Five runs per side is a useful starting point, not a statistical proof.
   Report run count, median, and spread; a difference within variation is inconclusive.
5. Check plausibility against resource limits and the changed work's share of
   total time. Pair a microbenchmark with a realistic end-to-end measurement when
   claiming a user-visible improvement.

Report the result, units, workload, run count, spread, and evidence for its cause.
Separate observed timing from causal inference and note gaps that prevent a fair
decision. Link the raw measurements instead of filling the final reply with logs.
For a user-requested ballpark, one labeled run can suffice; still verify the work
happened and its outputs were correct. Choosing between alternatives needs a
fair comparison. See [explain the number](../principles/explain-the-number.md).
