# Review

A review request produces findings; do not apply fixes unless the user requested
them. Establish the intended behavior and the exact diff or artifact under review.
Read surrounding callers, contracts, and existing tests before forming a verdict.

For a supplied review handoff, follow [review handoff](review-handoff.md) to check
its snapshot and return feedback for the author to record, or update the assigned
review notes when permitted. A review request does not authorize source fixes.

Review correctness, lifecycle and concurrency, compatibility, user experience,
and unnecessary complexity. Use [blast radius](blast-radius.md) for effects beyond
the diff, [reader load](../principles/minimize-reader-load.md) for structure, and
[behavioral tests](../principles/test-behavior-not-implementation.md) for test quality.

For an adversarial or multi-model request, ask available independent reviewers to
challenge the same intent and diff. Use only actual supported models and report
the participants. If independence is unavailable, say so and perform a local pass.

Validate candidate findings yourself. Each actionable finding needs a trigger,
impact, location, and evidence or a concrete reproduction. Prioritize confirmed
defects. Keep unresolved risks separate from proven failures. No findings does not
mean the feature was executed; report the limits of the review.
