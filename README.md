# kw-skills

KW's engineering mode for Claude Code and Codex. Ground the problem, choose a sound
shape, make the smallest useful change, and prove the result.

This toolkit adapts [pstack](https://github.com/cursor/plugins/tree/main/pstack)
and takes the shared-source installation pattern from
[deez-skills](https://github.com/daryl-tg/deez-skills). It has no dependency on Cursor.

## Use

In Claude Code:

```text
/kw-mode the form loses its draft when I switch tabs. Reproduce, fix, and verify.
/kw-mode let's discuss the data model before building this.
/kw-mode review this diff and check what it could break.
/kw-mode reflect on this session and improve the relevant workflow.
```

In Codex, use the same requests with `$kw-mode`.

The mode reads your request and chooses a playbook. It stays active for related
turns in that conversation until you opt out. A discussion remains a discussion;
implementation and delivery follow what you requested.

## Install

Requires Python 3.11 or later. Keep this directory at a stable location because
the installation uses symlinks to it.

```sh
git clone https://github.com/ykhaiwei/kw-skills.git
cd kw-skills
bin/doctor
bin/test
bin/link
bin/link --apply
bin/doctor --installed
```

`bin/link` previews without writing. `--apply` creates links for the registered
skills in `~/.claude/skills` and `~/.agents/skills`. It follows an existing symlink
on the skills directory, preserves other entries, and refuses to replace an
occupied skill name. Repeating installation is safe.

For one runtime, add `--runtime claude` or `--runtime codex` to `link` and to
`doctor --installed`. For an isolated installation check, use `--home /tmp/kw-test-home`.

Start a fresh Claude Code or Codex conversation after installation. If discovery
has not refreshed, restart that runtime. Local skill discovery and symlink support
are documented by [Claude Code](https://code.claude.com/docs/en/skills) and
[OpenAI](https://learn.chatgpt.com/docs/build-skills).

To remove only this hub's matching symlinks:

```sh
bin/link --remove
bin/link --remove --apply
```

This leaves the source and unrelated skills intact. Move the source by removing
its links first, moving the directory, and running the installer at its new path.

## What is included

One installed skill contains 23 engineering principles, 23 playbooks, and 15
supporting workflows. The references load when needed and do not become dozens
of separate entries in the runtime's skill catalog.

```text
skills/kw-mode/
  SKILL.md          entry point and routing
  profile.md        confirmed preferences and initial defaults
  runtime.md        native Claude/Codex tool mapping
  principles/       one engineering rule per reference
  playbooks/        task sequences and completion evidence
  workflows/        investigation, design, review, verification, reflection
  agents/openai.yaml
registry.toml       installed skills and runtime locations
upstream.json       source revision, provenance, and adaptation notes
bin/                link, doctor, test
tests/              installer and reference-integrity tests
```

Browse the [mode](skills/kw-mode/SKILL.md) for the complete routing tables and the
[principles index](skills/kw-mode/principles/index.md) for the engineering rules.
The supporting workflow names are arguments to `kw-mode`, not standalone commands.

## Make it yours

Edit [profile.md](skills/kw-mode/profile.md) for personal choices. Keep common
engineering rules in their principle leaves and task sequences in playbooks.
Put project-specific requirements in the project. Add a separate registered skill
only when it needs independent discovery or invocation.

The initial defaults inherit your current model, use native delegation when
available and permitted, and follow the project's delivery conventions. There are
no hardcoded model subscriptions, cross-CLI dispatches, custom agent dependencies,
always-on loops, permission overrides, or external posting destinations.

`bin/doctor` checks frontmatter names, registry coverage, contained and reachable
references, upstream provenance, and optionally installation targets. `bin/test`
exercises actual installation and removal in temporary directories, including
conflicts, shared directories, and broken references. Neither proves the quality
of a future model's decisions. Validate substantive instruction changes on real
tasks, using the [eval playbook](skills/kw-mode/playbooks/eval.md) when appropriate.

## Upstream and updates

The principle text derives from pstack at commit
`27e2a62ff94f9af4b5e68435e41cdceacadb840c`. Playbooks and supporting workflows are
portable adaptations, not a drop-in copy of every upstream automation.

The 23 general playbook categories are preserved. Cursor-specific cloud agents,
model slugs, loop commands, and team-kit dependencies are replaced by native
runtime capabilities and local workflows. Delivery follows session authorization
and repository policy. Bot automations and product-specific deez workflows are
outside this baseline.

`upstream.json` records original paths and source hashes. To update, compare the
pinned files with a chosen newer upstream revision, review changes against the KW
profile/runtime contract, update the affected references and provenance, then run
`bin/doctor` and `bin/test`. No background updater rewrites personal choices.

Pstack's MIT attribution is preserved in [LICENSE](LICENSE). Deez-skills informed
the hub architecture; no source code from that repository is copied here.
