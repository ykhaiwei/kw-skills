# Feature

1. Define the user's observable outcome and its acceptance cases. Read the existing
   subsystem with [how](../workflows/how.md), including surrounding conventions.
2. Name the data shape and ownership using [model the domain](../principles/model-the-domain.md).
   Use [architect](../workflows/architect.md) before locking in new interfaces.
3. Establish how the feature will be exercised. Reuse the nearest harness; build a
   small verification tool if the new behavior otherwise cannot be observed.
4. Implement in [verifiable units](../principles/sequence-verifiable-units.md).
   Before delegation, identify blocking checks, independent workstreams, shared
   mutable state, and the smallest safe decomposition. Keep shared writers isolated.
   Subtract obsolete paths where safe. Keep speculative features outside the diff.
5. Exercise the actual user flow with [verify](../workflows/verify.md), including
   relevant error, empty, persistence, or lifecycle cases. Inspect UI appearance
   and interaction on the intended viewport when the feature is visual.
6. Run [review](../workflows/review.md) and resolve confirmed defects. Complete the
   authorized delivery through [opening a PR](opening-a-pr.md).

Reply with the resulting behavior, design tradeoff, real verification, and status.
