# Review

A review request produces findings; do not apply fixes unless the user requested
them. Establish the intended behavior and the exact diff or artifact under review.
Read surrounding callers, contracts, and existing tests before forming a verdict.

For a supplied review handoff, follow [review handoff](review-handoff.md) to check
its snapshot and return feedback for the author to record, or update the assigned
review notes when permitted. A review request does not authorize source fixes.

## Challenge the reasoning

Reconstruct the user's intended outcome from the task and source before reading
the author's rationale as justification. Identify the consequential assumptions:
what must be true for this design to work, and what evidence could disprove it?
Trace the affected behavior through callers, state changes, and failure paths.
Prioritize likely failures and costly consequences; do not exhaust every possible
decision or invent objections to make the review look thorough.

For a material design choice, consider a simpler alternative and explain the
concrete tradeoff. A stylistic preference alone is not a defect or a reason to
reopen a settled user decision. Distinguish a wrong implementation from a missing
requirement, an unsupported assumption, and an optional improvement.

Investigate facts with the available tools before asking questions. For an
implementation review, direct technical challenges to the author, identifying the
assumption, its consequence, and the evidence or experiment that would settle it.
Return unresolved challenges with the findings so the author can answer them in
the handoff. An assertion alone does not establish correctness.

Escalate to the user only an unresolved intent, preference, or authorization that
materially changes the result. Include a recommendation and its tradeoff; group
independent decisions and defer questions that depend on an unanswered decision.
Continue work that does not depend on the answer. An unavailable fact or check is
a verification gap to report, not a preference for the user to guess.

## Inspect and report

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
