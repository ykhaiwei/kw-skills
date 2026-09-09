# kw-skills

My engineering mode for Claude Code and Codex. Understand the problem, build less,
and verify the result.

## Install

Requires Python 3.11+.

```sh
git clone https://github.com/ykhaiwei/kw-skills.git
cd kw-skills
bin/link --apply
bin/doctor --installed
```

Start a new Claude Code or Codex conversation. Keep the repo where you cloned it;
the installed skills link back to it.

## Use

Claude Code:

```text
/kw-mode fix this bug and verify it
/kw-mode review this diff
/kw-mode let's discuss the approach first
```

In Codex, use `$kw-mode` instead.

Edit [profile.md](skills/kw-mode/profile.md) to customize the defaults.
