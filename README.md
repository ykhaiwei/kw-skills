# kw-skills

My engineering mode for Claude Code and Codex. Understand the problem, build less,
and verify the result.

## Install

```sh
git clone https://github.com/ykhaiwei/kw-skills.git
cd kw-skills
```

Open this folder in Claude Code or Codex and say:

```text
set it up
```

Agents: treat that as a request to follow [AGENTS.md](AGENTS.md) and the
[setup guide](docs/new-computer-setup.md). Check prerequisites, install KW mode
as the default for Claude Code and Codex, preserve existing settings, and verify
the installation. Handle routine setup and report any remaining user actions.

To install manually instead, use Python 3.11+ and run:

```sh
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

Moving computers? Give your agent the [setup guide](docs/new-computer-setup.md),
which includes a copy-paste prompt.

KW mode checks for upstream updates weekly when you use it. To check sooner, ask:
`check for useful upstream updates to kw-mode`. Changes are reviewed before import.
