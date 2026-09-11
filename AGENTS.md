# Working in kw-skills

Use [KW mode](skills/kw-mode/SKILL.md) as the default workflow for work in this
repository. Read it before substantive work, then load the references relevant
to the task. The user does not need to invoke a command. Keep casual replies
lightweight and honor task-specific opt-outs.

## Setup

For a new computer or a migration, follow the
[new-computer guide](docs/new-computer-setup.md) for prerequisites, installation,
conflict handling, and fresh-session verification.

When the task includes installing or repairing this setup, run from the repo root:

```sh
bin/setup
bin/setup --apply
bin/doctor --installed --defaults
```

The preview shows skill links and the exact global instruction block. Setup links
the shared skill and adds that block to Claude Code and Codex user instructions.
It preserves surrounding instructions and is safe to repeat. Add
`--runtime claude` or `--runtime codex` when only one runtime is requested.
New sessions inherit the default; the current task can read the mode directly.

`bin/setup --remove --apply` removes this installation's links and default blocks.
`bin/link` manages only skill links. Keep this checkout at a stable path.

## Maintenance

For a requested upstream update check, use the
[review playbook](skills/kw-mode/playbooks/upstream-review.md) and maintain the
[review log](docs/upstream-reviews.md) so later checks retain pending decisions.

The skill and its references are the source of truth. Global instructions should
remain a short pointer, not another copy of the playbooks. Edit
[profile.md](skills/kw-mode/profile.md) for working preferences and
[runtime.md](skills/kw-mode/runtime.md) for host behavior and maintenance paths.

Run `bin/doctor` for instruction/reference edits and `bin/test` for tooling changes.
Exercise installation tests in a temporary home, never against real user settings.
Keep installation reversible and preserve unrelated files and user instructions.
Record original references with local provenance and describe adaptations accurately.

Follow the user's current commit and publication instructions. A setup or repair
request does not by itself request a commit or push.
