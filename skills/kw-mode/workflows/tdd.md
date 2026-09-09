# TDD

Use a failing test first for a defect with a practical local test path.

1. Name intended behavior, observed behavior, and the smallest reproduction.
2. Choose the closest existing unit, component, integration, or regression harness.
3. Write a check of observable behavior and run it before production edits. Confirm
   that it fails because of the defect, not a missing fixture or broken setup.
4. Make the smallest sound fix, rerun the regression, then nearby relevant checks.

Follow [test behavior](../principles/test-behavior-not-implementation.md). Do not
change an expectation just to accommodate a wrong implementation.

If a test needs disproportionate infrastructure, use a focused script, browser
reproduction, log assertion, or output comparison instead. State the limitation
and keep useful evidence. A token test of mocks is worse than an honest runtime check.
