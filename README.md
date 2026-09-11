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
[setup guide](docs/new-computer-setup.md). Check prerequisites, install kw mode
as the default for Claude Code and Codex, preserve existing settings, and verify
the installation. Handle routine setup and report any remaining user actions.

To install manually instead, use Python 3.11+ and run:

```sh
bin/setup --apply
bin/doctor --installed --defaults
```

After setup succeeds, start a new Claude Code or Codex conversation. The global
instructions make kw mode the default across projects. Keep the repo where you
cloned it; the installation links back to it.

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

kw mode asks your agent to check for upstream updates when its weekly interval
is due. To check sooner, ask: `check for useful upstream updates to kw-mode`.
Changes are reviewed before import; nothing runs while your assistants are closed.

After substantial changes, kw mode automatically requests a review from the
opposite runtime—Codex to Claude, Claude to Codex—using its strongest available
model. If unavailable, it uses a fresh reviewer in the current runtime. The
original agent fixes confirmed findings and prepares logical commits. Local
review notes stay out of Git; commits and pushes follow your requested scope.

[MIT licensed](LICENSE).
