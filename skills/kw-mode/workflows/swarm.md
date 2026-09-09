# Swarm

Define the whole-task acceptance condition, partition the work into independent
slices, and give each slice a named owner and return artifact. Use the
[runtime contract](../runtime.md) and [separate shared state](../principles/separate-before-serializing-shared-state.md).
Keep verification criteria outside each worker's write scope.

Dispatch only as many workers as the host permits. Each returns completed scope,
evidence, changed paths, and blockers. Keep useful local integration work with the
lead. For competing attempts at one problem, use [arena](arena.md) instead.

Account for every required slice. A failed or missing worker is a coverage gap to
resolve, not a reason to declare the remaining slices complete. Review outputs,
check cross-slice boundaries, and return one consolidated result with explicit gaps.
