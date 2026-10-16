# Test Behavior, Not Implementation

Test what a caller, end user, or another service can observe through its interface: returned values, errors, readable state, and external effects. Private helpers, internal call order, and intermediate data are implementation details unless the public contract makes them observable.

Judge a test with two imagined changes:

- Break the behavior it claims to protect: return the wrong value, skip the effect, or perform it twice. The test should detect that defect. If it does not, strengthen the assertion or narrow the claim.
- Change the internals while preserving that behavior. The test should still pass. If it fails, remove coupling to internal structure.

Drive the subject with a concrete input and derive the expected result from the requirement, independently of the code under test. Avoid assertions on fixtures that never exercise the subject, self-computed expectations, and copies of constants or prompt strings that do not test their use.

The contract determines whether an assertion is meaningful. No charge for an empty cart is real behavior; pair that check with a case that charges to show the observer works. A mocked external service's received payload is observable behavior; a private helper's call count usually is not. An empty result can be the exact promised answer. Assert error wording when wording is part of the contract; otherwise prefer the error type or code callers use.

Schema relationships and compile-time checks can protect real invariants. Keep tests that catch meaningful contract violations and survive behavior-preserving refactors; rewrite or remove tests that provide no such protection.
