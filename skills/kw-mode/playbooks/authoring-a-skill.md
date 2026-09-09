# Authoring a skill

1. Name the recurring task or decision the instruction should change. Read the
   existing skill and its callers before editing it.
2. Use the current host's skill-authoring guidance when available. Keep discovery
   metadata narrow; put conditional procedures in linked references.
3. Preserve the user's scope, runtime capabilities, and authorization. Encode a
   repeated mechanical failure in a check when possible, following
   [encode lessons](../principles/encode-lessons-in-structure.md).
4. Validate frontmatter, paths, and referenced capabilities. Run changed scripts.
   Use realistic behavior checks for material workflow changes, not tests that
   merely assert the instruction's wording.
5. Review the diff with [writing](../workflows/writing.md), then complete requested
   installation or delivery. For this hub, run `bin/doctor` and `bin/test`.
