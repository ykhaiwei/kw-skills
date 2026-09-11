# kw profile

## Confirmed choices

- Name: `kw-mode`. Keep `kw` lowercase in headings, display names, and prose.
- Apply automatically to substantive work in every session. No slash command is
  required. Keep casual conversation lightweight and respect explicit opt-outs.
- Claude Code is the primary runtime; Codex is also used. No Cursor dependency.
- Keep pstack's philosophy and general workflow as the baseline, then build on it.
- Use deez-skills as a reference for a shared, maintainable skill hub.
- Check pstack automatically when kw mode starts substantive work and the weekly
  interval is due; explicit checks can run sooner. Use
  [weekly upkeep](workflows/weekly-upkeep.md) and selectively adapt useful ideas
  when requested. Keep review history separate from imported provenance.
- After substantial implementation, automatically run the
  [review handoff](workflows/review-handoff.md): review with the opposite runtime's
  strongest available model, fall back to a fresh reviewer in the current runtime,
  fix confirmed findings, and prepare logical commits. The original agent owns
  fixes and commit preparation. Keep review notes out of the public repository.
- For this hub, keep verification scripts temporary and remove them after checks
  pass, recording results in the review handoff. Preserve other projects' existing
  test conventions and suites.

## Initial defaults

These are starting choices, not preferences inferred from private history.

- Inherit the current runtime's model for implementation. Automatic independent
  review follows the opposite-runtime preference above.
- Use native delegation when available, permitted, and useful for a bounded task.
  The lead retains responsibility for design, integration, review, and verification.
- Follow each project's verification and delivery conventions. No universal
  squash policy, public posting destination, or fixed development port.
- Keep skills and references here as the single maintained source. Add project
  specifics in the project rather than turning them into universal rules.

To customize, ask `kw-mode` to update this profile with the specific preference.
For lessons from completed work, use [reflect](workflows/reflect.md). Record the
reason for a durable change; do not infer a working style from a GitHub profile.
