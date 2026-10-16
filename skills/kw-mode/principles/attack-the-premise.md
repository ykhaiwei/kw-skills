# Attack the Premise

When two or more fixes that share one premise fail the same gate, test the premise before writing another fix that assumes it. Repeated failure is evidence to investigate, not proof that the premise is false.

- Write the shared premise in one sentence.
- Find an observation that would differ if it were false, and make that observation. Examine the distribution of failures as well as their size. Make the check rerunnable when useful per [Build the Lever](build-the-lever.md).
- If the evidence contradicts the premise, revise it and investigate what the failures share. If it supports the premise, ask the next why per [Fix Root Causes](fix-root-causes.md); the fixes may have addressed a consequence. State unresolved uncertainty when the observation does not distinguish the alternatives.
- Remove the condition that produces the failure where possible, rather than repeatedly compensating for it. When particular actors consistently lose, investigate what assigns that role. An even distribution alone does not rule out the premise.

Do not start the next speculative fix until the premise and the result of its test are recorded. [Redesign from First Principles](redesign-from-first-principles.md) rebuilds a design around a requirement; this principle checks a fact the current design assumes.
