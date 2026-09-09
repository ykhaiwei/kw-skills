# Autopilot full

1. Freeze the queue of independent deliverables and establish whether the user
   authorized review creation and landing for each. Split dependent work into a stack.
2. Give each deliverable one owner, isolated worktree, acceptance contract, and
   clear return artifact using [swarm](../workflows/swarm.md).
3. Drive each item through its implementation playbook, verification, and
   [opening a PR](opening-a-pr.md). Keep failed or blocked items visible in the queue.
4. Independently inspect the actual diff and verification at each current head.
   Resolve integration or shared-resource conflicts before advancing.
5. Land only authorized, verified items via [shipping](shipping.md), confirming each
   outcome. Otherwise stop those items at the requested local or review-ready state.
6. Account for every queue item with its evidence and final state. Do not mark the
   queue complete while required items remain unverified or blocked.
