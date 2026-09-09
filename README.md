# kw-skills

My engineering mode for Claude Code and Codex. Understand the problem, build less,
and verify the result.

## Install

Requires Python 3.11+.

```sh
git clone https://github.com/ykhaiwei/kw-skills.git
cd kw-skills
bin/setup --apply
bin/doctor --installed --defaults
```

Start a new Claude Code or Codex conversation. KW mode is now the default across
projects. Keep the repo where you cloned it; the installation links back to it.

## Use

Just describe the task:

```text
fix this bug and verify it
review this diff
let's discuss the approach first
```

No command needed. `/kw-mode` in Claude Code and `$kw-mode` in Codex still work.
Say "skip kw-mode for this task" to opt out.

Edit [profile.md](skills/kw-mode/profile.md) to customize the defaults.
Agents can start with [AGENTS.md](AGENTS.md) for setup and maintenance.
