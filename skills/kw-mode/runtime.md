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

### Automatic review across runtimes

For [review handoffs](workflows/review-handoff.md), use the opposite runtime first.
Resolve the installed CLI and read its help before choosing flags. Keep the author
in the current runtime; only the independent review crosses to the other runtime.

When supported, Claude's `best` alias selects its most capable available family; see
[model configuration](https://code.claude.com/docs/en/model-config). For Codex,
resolve its strongest available coding model from the runtime's model catalog
and [model guidance](https://learn.chatgpt.com/docs/models). Do not sort model IDs
lexically or select a hidden approval model. Record the actual model reported by
the invocation and disclose any model fallback.

Use a fresh noninteractive session, a review-only prompt, and source read access.
Pass the brief on stdin and capture feedback to a file; avoid shell-interpolating
the user's task or source text. For installed versions supporting these options:

```sh
claude -p --model best --effort high --safe-mode --no-session-persistence \
  --permission-mode dontAsk --tools Read,Glob,Grep --output-format json \
  < "$review_brief" > "$review_result"

codex exec --model "$review_model" --sandbox read-only --ephemeral \
  --output-last-message "$review_result" - < "$review_brief"
```

Run from the reviewed project. `review_brief`, `review_result`, and `review_model`
are task-specific values resolved by the author, not literal placeholders to send
to the model. The Claude example disables customization and code-running tools;
include project instruction paths explicitly and provide the diff as a readable
artifact. The reviewer must disclose checks it could not execute. Read Codex's
active configuration for hooks or integrations before launch; a read-only sandbox
does not itself disable host hooks. Use supported per-session restrictions or the
native fallback if the review cannot be kept within scope. Do not bypass approval
or sandbox restrictions to run a review.

CLI versions and account access vary. If an option or model is unsupported, adapt
to verified equivalent controls or use the native fallback. A native reviewer
gets the same review-only contract and no authority to fix, delegate, or commit.
Do not recursively run the full default workflow inside a dispatched reviewer.

### Responsibilities

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
