# Shipping

1. Establish the authorized landing scope, actual forge, target branch, and repository
   merge policy. Freeze the list of reviews to land and their dependency order.
2. Review and [verify](../workflows/verify.md) every candidate at its recorded base
   and head. Use an independent reviewer when available. Keep unresolved verdicts
   and missing runtime evidence visible; CI alone is not behavioral proof.
3. For a dependent stack, find the contiguous verified run starting at its bottom.
   Stop the landable run at the first unverified dependency.
4. Before each merge, re-read head, base, checks, and mergeability. Re-verify changes
   since the verdict. A stable patch identity can preserve a code-review verdict
   across a pure rebase, but integration checks still need the current base/head.
5. Land one review at a time through the forge using the project's required method.
   Arm auto-merge only within an authorized merge-when-ready request. Confirm the
   actual merged state; queued or approved is not merged.
6. Refresh the remaining dependencies after each merge. Verify retargeted bases and
   changed integration state before proceeding. Do not arm descendants speculatively.
7. Stop at the authorized verified boundary. Report what landed, what remains, and
   the exact blocker or evidence needed next.
