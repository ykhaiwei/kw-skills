# kw-skills

My engineering mode for Claude Code and Codex. Understand the problem, build less,
and verify the result.

## Setup

```sh
git clone https://github.com/ykhaiwei/kw-skills.git
cd kw-skills
```

Open the folder in Claude Code or Codex and say **“set it up.”**
Agents follow [AGENTS.md](AGENTS.md) and the [setup guide](docs/new-computer-setup.md).
The guide also covers manual installation and moving to another computer.

Once setup finishes, start a new conversation. kw mode becomes the default across
projects. Keep this checkout in place; the installed skills link back to it.

## Use

Describe what you need: fix a bug, review a diff, or stress-test a plan. kw mode
investigates the problem, challenges assumptions, and verifies the result.
Design discussions stay discussions until you ask for implementation.

For substantial changes, your agent requests an
[independent review](skills/kw-mode/workflows/review-handoff.md) from the other
runtime when available. It handles technical feedback and prepares commits,
bringing you decisions that need your input. Commits and pushes follow your
instructions.

No command is required. `/kw-mode` in Claude Code and `$kw-mode` in Codex are
optional. Say “skip kw-mode for this task” to opt out.

Customize [profile.md](skills/kw-mode/profile.md) to change the defaults.
[Upstream checks](docs/upstream-reviews.md) run when you use the mode and the weekly
interval is due. Updates are reviewed before adoption.

[MIT licensed](LICENSE).
