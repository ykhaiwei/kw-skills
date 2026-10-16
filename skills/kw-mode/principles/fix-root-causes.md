# Fix Root Causes

Trace the symptom to the first place the system made a wrong decision or failed to handle a state it should support. A fix belongs there; hiding the symptom leaves the fault available to surface elsewhere.

- Reproduce the failure and inspect the actual error and state. Instrument when the evidence is missing.
- Ask why at each step until the answer identifies the fault, rather than a consequence of an earlier one.
- Decide whether the triggering state is legitimate. If the system must support it, handling it is a root-cause fix. If it violates an invariant, find what produced it. Guards, retries, clamping, swallowed errors, and discarded state can conceal that producer; judge them by the contract rather than banning their syntax.
- For restart-only failures, inspect persisted configuration, caches, locks, and serialized state before changing code. Preserve diagnostic evidence before cleanup.
- Search for the same fault elsewhere and fix confirmed instances within the requested scope. Record unrelated findings.
- Treat a workaround needing extensive justification as a reason to revisit the cause; comment length alone does not establish that the code is wrong.
- When a decisive fact required a deep investigation, propose a cheap ongoing signal that would expose it sooner, such as a focused counter, log field, or state check. Add it when useful and within scope.
