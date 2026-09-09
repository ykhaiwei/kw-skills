# Multi-phase plan

1. Ground the proposed work in actual source and constraints. Name the outcome,
   excluded scope where material, unresolved decisions, and acceptance evidence.
2. Order phases by dependency and uncertainty. Resolve foundational design and the
   verification path before dependent implementation.
3. For each phase, specify its deliverable, affected boundaries, prerequisites,
   verification, and what would block or invalidate the approach. Keep each phase
   independently reviewable using [verifiable units](../principles/sequence-verifiable-units.md).
4. Identify safe parallel work, shared ownership, compatibility obligations, and
   delivery constraints. Use [architect](../workflows/architect.md) for open interfaces.
5. Write the plan at the project's established location, otherwise a task-owned
   scratch path. Report concrete choices and remaining decisions. A plan-only
   request stops here; execution uses [autonomous run](autonomous-run.md) or
   [orchestrate](orchestrate.md) when authorized.
