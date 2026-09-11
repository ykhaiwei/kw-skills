# Runtime contract

Resolve paths relative to this skill's real directory, following its installation
symlink. Pass absolute reference paths to delegates so they can find the same
instructions. Supporting markdown files are read with the host's file tools.

For hub maintenance, the repository root is two parent directories above this
resolved skill directory. Run `<hub-root>/bin/doctor` by absolute path, or run
`bin/doctor` from that root. Do not resolve this command against the project
currently being worked on. For this hub's tooling changes, use temporary behavior
checks, record the results in the review handoff, and remove the checks afterward.

## Claude Code

Global user instructions load the default; `/kw-mode <task>` remains an optional
explicit invocation. Use the native task list and subagent tool available in
the running version. Prefer the built-in explorer for scoped read-only source
discovery and a general-purpose agent for implementation. Inspect available agent
types before naming a specialized role; the role names below are responsibilities,
not registered agent identifiers. Omit a model override to inherit the session.

## Codex

Global user instructions load the default; `$kw-mode <task>` remains an optional
explicit invocation. Use the available planning and delegation tools. Do not
assume a `Task` API, Claude agent definitions, or a particular `agent_type` exists.
Map the responsibility to a supported tool or execute it locally. Inherit the
parent model unless the user or project explicitly selected another available one.

## Roles and handoffs

| Responsibility | Output |
| --- | --- |
| Explore | A traced explanation with file and symbol evidence |
| Implement | A bounded diff against a stated behavior contract |
| Test | An executable check and its observed failure/pass |
| Review | Prioritized findings, triggers, and evidence |
| Verify | Independent observations on the changed artifact |

Delegate only when the host and current instructions permit it. Keep work in the
runtime the user chose. Use independent workers for separable work or competing
approaches; do not delegate a single obvious edit to manufacture parallelism.
Respect actual concurrency limits. Serial work is a valid fallback; disclose when
an independent or multi-model review could not be obtained.

Every handoff includes the goal, scope, relevant source and reference paths,
allowed writes, verification criteria, and required return artifact. Isolate
writers by worktree or non-overlapping ownership. The lead inspects results and
performs integration checks. Use the current host's native wait/resume facilities;
do not invent background persistence or promise work after the session has ended.

## Tools and integrations

Discover the repository's actual build, test, browser, CLI, and forge tools. Use
installed specialist skills when relevant, but no named third-party skill is a
required dependency of this bundle. Local workflow references provide the baseline.

Use the repository's remote to choose GitHub or GitLab tooling. A tool being
installed does not establish its authorization or select a posting destination.
Keep existing authentication and runtime configuration intact.
