# Orchestrate

1. Define the program's end state, scope, acceptance evidence, dependencies, and
   authorized delivery. Record a durable plan using [multi-phase plan](multi-phase-plan.md).
2. Establish one coordinator and clear ownership for each independently verifiable
   unit. Use [swarm](../workflows/swarm.md) under the host's real concurrency limits.
3. Give workers self-contained briefs and isolated writable resources. Keep shared
   interfaces and verification contracts under coordinator ownership.
4. Review artifacts, verify integrations, and update the dependency map after each
   completed unit. A worker's completion report is not the program's acceptance test.
5. Keep current progress, decisions, evidence, blockers, and next actions in a
   [decision trail](../workflows/show-me-your-work.md). Reconcile live state on pickup.
6. Route independent deliveries to [autopilot full](autopilot-full.md) or dependent
   changes to [autopilot stack](autopilot-stack.md) only when their scope fits.
7. Verify the full program against the original end state. If the session must
   stop first, leave a [resumable checkpoint](pause-safely.md) rather than imply a
   persistent coordinator exists outside the host session.
