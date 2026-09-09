# Bug fix

1. Reproduce the defect on the affected surface. Capture intended and actual
   behavior and the preconditions. Read [fix root causes](../principles/fix-root-causes.md).
2. Use [how](../workflows/how.md) to trace the failure to its cause. Investigate
   historical intent through [why](../workflows/why.md) when necessary. When program
   state is unclear, instrument it and inspect the observations as the code runs.
3. Establish the regression check with [TDD](../workflows/tdd.md). Confirm it fails
   for the right reason, or document a practical executable alternative.
4. Fix the root cause with the smallest sound change. Use
   [architect](../workflows/architect.md) if the fix changes ownership or interfaces.
5. Rerun the reproduction and relevant neighboring cases with
   [verify](../workflows/verify.md). Review the diff using [review](../workflows/review.md).
6. Finish the requested delivery through [opening a PR](opening-a-pr.md), including
   local-only delivery when no external review was requested.

Reply with the cause, changed behavior, regression evidence, and delivery status.
