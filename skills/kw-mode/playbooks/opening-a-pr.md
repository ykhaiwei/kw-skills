# Opening a PR

This is the delivery checkpoint for implementation playbooks. It does not expand
the requested scope. A local fix may finish here without a commit or external PR.

1. Inspect the final diff and working state. Preserve unrelated changes. Apply
   [review](../workflows/review.md) and [writing](../workflows/writing.md), and resolve
   confirmed defects. Verify the final artifact, not a previous revision.
2. Follow repository conventions for branches, commits, and review size. Use
   [verifiable units](../principles/sequence-verifiable-units.md) for a dependent
   sequence. Do not invent a stack for a small independent change.
3. Prepare a concise review description: the problem, resulting behavior, material
   tradeoffs, and actual validation. Follow the repository template where present.
4. If opening a review is authorized, resolve the forge from the actual remote,
   use its installed tool, and create the requested draft or ready review against
   the correct base. If not, deliver the local artifact and prepared description.
5. Read back any created review and report its real URL and status. Opening it does
   not initiate merging or an indefinite watch. Use [babysit](babysit.md) when that
   additional work is requested.
