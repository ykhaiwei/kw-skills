# Reflect

Improve this mode from evidence in completed work when the user asks to reflect
or update their working conventions.

1. Read the active conversation or a user-specified, project-scoped record. Identify
   repeated corrections, wasted work, missed checks, and useful techniques.
2. Separate explicit user preferences from inferences. Do not promote a one-off
   workaround into a universal rule. State the evidence for a proposed change.
3. Prefer a deterministic check or tool when it prevents the repeated failure.
   Otherwise edit the smallest relevant principle, playbook, workflow, or
   [profile](../profile.md). Read [encode lessons](../principles/encode-lessons-in-structure.md).
   Read the target before editing: improve weak wording or routing instead of
   duplicating an existing rule. Favor ownership or type changes that prevent
   the bad state, then a focused check; show that it catches a real past mistake.
4. Apply requested corrections within their scope. If the user requested proposals
   only, present the draft. Do not rewrite unrelated installed skills.
5. Run `bin/doctor` from the hub root, resolved through [runtime](../runtime.md),
   and any relevant script tests. Explain which decision will change next time
   and what evidence motivated it.
