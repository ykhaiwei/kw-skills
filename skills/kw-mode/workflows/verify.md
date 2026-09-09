# Verify

1. State the user-observable claim and the case that could disprove it. Identify
   the exact artifact, revision, environment, and preconditions being tested.
2. Use the repository's closest reliable harness. For a UI, drive the changed
   interaction; for a CLI, invoke the command and inspect output and state; for an
   API, send a request and inspect its effects. Check persistence or restart when
   the behavior depends on them.
3. Run the original failing case and meaningful neighboring cases. Use real code
   at the boundary under test. Label simulations, mocks, and unavailable services.
4. Preserve commands, results, and relevant screenshots, logs, or measurements.
   A screenshot proves appearance, not a hidden state transition.
5. Check the final diff. If the artifact changes after verification, rerun affected
   checks. Report passed, failed, and unverified claims separately.

Read [prove it works](../principles/prove-it-works.md). Compiler success and a
delegate's self-report are not substitutes for behavior evidence. If no harness
exists, add the smallest rerunnable check that earns its maintenance cost using
[build the lever](../principles/build-the-lever.md).
