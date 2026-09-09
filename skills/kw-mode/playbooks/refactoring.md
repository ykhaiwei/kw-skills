# Refactoring

1. Trace the existing contract with [how](../workflows/how.md). Capture it in a
   characterization test, output baseline, or equivalence harness before moving code.
2. Name the target structure and how it lowers [reader load](../principles/minimize-reader-load.md).
   Keep a clear existing shape when an extra abstraction would not improve it.
3. Use [architect](../workflows/architect.md) for substantive interface changes.
   [Subtract](../principles/subtract-before-you-add.md) dead weight before adding layers.
4. Move in small steps that keep the behavior check passing. Migrate internal
   callers and remove the obsolete API together; preserve supported public contracts.
   Check string references and documentation as well as typed symbol references.
5. Prove equivalence on the actual artifact using [verify](../workflows/verify.md).
   Review the final diff and remove changes that do not earn their complexity.
6. Complete the authorized delivery through [opening a PR](opening-a-pr.md).

Reply with the structural improvement, pinned contract, equivalence proof, and status.
