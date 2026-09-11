# kw mode on a new computer

Give this file to an AI agent with terminal access on the new computer. The
repository is <https://github.com/ykhaiwei/kw-skills>. These instructions restore
kw mode as the default engineering workflow for Claude Code and Codex.

## Copy-paste prompt

```text
Set up my kw mode on this computer from
https://github.com/ykhaiwei/kw-skills.

Read the repository's AGENTS.md and docs/new-computer-setup.md. If I attached
the guide, use that too. Inspect this machine, reuse a suitable existing checkout
or clone into a stable location, and install kw mode for Claude Code and Codex.
I mainly use Claude Code. Preserve my existing settings and unrelated skills.

Check prerequisites and use current official installation instructions for any
missing tools. Run the setup preview, apply it, and verify the skill links and
global defaults. Make routine setup decisions yourself. Ask only if something
needs my login, a system approval, or a choice you cannot infer safely. Do not
overwrite conflicting files or discard local changes.

Check fresh-session behavior if you can; otherwise give me the exact check to
run. Tell me where you installed it, what passed, and anything I still need to
do. Do not commit or push changes as part of setup.
```

For only one assistant, replace “Claude Code and Codex” with the one you want.
If the agent cannot access the computer, use an agent that can run local commands
or follow the commands below yourself.

## What comes with it

The checkout contains the skill, engineering principles, playbooks, workflows,
preferences, runtime guidance, and installer. Setup creates local skill links
and a short managed block in each assistant's global instruction file. That
block tells new sessions to read kw mode automatically for substantive work.

It does not migrate assistant accounts, API keys, MCP connections, other plugins
or skills, projects, or conversation history. Install and sign in to the actual
Claude Code or Codex application separately when needed. A plain web chat does
not read these local files.

You do not need to uninstall anything on the old computer. Each computer has its
own installation pointing at its own checkout.

## Before leaving the old computer

Check `git status` in the old checkout. Any preferences or skill changes you want
on the new computer must be in GitHub or transferred in a separate backup.
Uncommitted changes and ignored files do not arrive through `git clone`.

Keep private settings and credentials in a private backup. This repository is
public. Recreate skill links and managed defaults with setup on the new machine;
copying the old links or their absolute paths will point at the wrong location.

## Agent procedure

### 1. Inspect the environment

Read [AGENTS.md](../AGENTS.md) and [kw mode](../skills/kw-mode/SKILL.md).
Inspect the OS, shell, home directory, existing checkout, existing skill links,
and global instructions. Check for custom runtime homes and symlinked parent
directories before deciding where changes will land.

The installer requires Git for cloning and Python 3.11 or newer. It uses only
Python's standard library; no package installation or virtual environment is
needed. On macOS, Linux, or WSL, check:

```sh
git --version
python3 --version
```

Use a verified Python 3.11+ executable throughout. If a runtime is missing, use
the current official [Claude Code setup guide](https://code.claude.com/docs/en/setup)
or [Codex setup guide](https://learn.chatgpt.com/docs/quickstart).
Check installed apps as well as command-line tools; an absent CLI alone does
not establish that a desktop app is missing. Account login may need the user.

Run setup in the environment where the assistant runs. Native Windows and WSL
have separate homes; installing in one does not configure the other. Do not
silently move a native Windows setup into WSL.

### 2. Get a stable checkout

Use an existing checkout if its remote is this repository. Inspect its working
state before updating; preserve local changes. For a new checkout on macOS,
Linux, or WSL, a suitable location is:

```sh
mkdir -p ~/code
git clone https://github.com/ykhaiwei/kw-skills.git ~/code/kw-skills
cd ~/code/kw-skills
```

Choose another stable directory if that path is already occupied. Avoid temporary
folders. The installed skill links and global instructions refer to this path,
so the checkout must remain available.

### 3. Validate, preview, and install

Run from the checkout root:

```sh
python3 bin/kw.py doctor
python3 bin/kw.py setup
python3 bin/kw.py setup --apply
python3 bin/kw.py doctor --installed --defaults
```

Read the preview before applying. It shows the destinations and exact global
instruction block. Resolve validation failures or unexpected destinations first.
Preview alone makes no changes. Repeating setup is safe when the existing links
belong to this checkout, and it preserves instructions outside its managed block.

The shorter `bin/setup` and `bin/doctor` commands are aliases for this Python
entrypoint. `bin/link` installs skill links only; use `setup` to enable defaults.

To configure only Claude Code, use:

```sh
python3 bin/kw.py setup --runtime claude
python3 bin/kw.py setup --runtime claude --apply
python3 bin/kw.py doctor --runtime claude --installed --defaults
```

Use `--runtime codex` instead for Codex only. Keep the same runtime selection
across preview, apply, and installed verification.

### 4. Understand the installed paths

Here `~` means the home of the user running the assistant in this environment.

| Purpose | Default path |
| --- | --- |
| Shared source | `<checkout>/skills/kw-mode/` |
| Claude Code skill link | `~/.claude/skills/kw-mode` |
| Codex skill link | `~/.agents/skills/kw-mode` |
| Claude Code global instructions | `~/.claude/CLAUDE.md` |
| Codex global instructions | `~/.codex/AGENTS.md` |

The installer honors `CODEX_HOME` for Codex global instructions when installing
into the real user's home. It uses a nonempty `AGENTS.override.md` there in
preference to `AGENTS.md`. The Codex skill link remains under `~/.agents/skills`.
See the official [Codex instruction lookup](https://learn.chatgpt.com/docs/agent-configuration/agents-md)
and [skill locations](https://learn.chatgpt.com/docs/build-skills).

Claude Code's standard global instructions are described in its
[memory guide](https://code.claude.com/docs/en/memory). This installer currently
targets the standard `~/.claude` paths. If Claude uses a custom configuration
directory, investigate its actual lookup and adapt deliberately; do not report
success just because files exist in the standard location.

`--home` isolates installer tests. It does not tell either assistant to read a
different home and should not be used as a substitute for configuring a runtime.

### 5. Verify a fresh conversation

The final doctor command must pass for the selected runtimes. It verifies the
source, skill links, and managed instruction blocks. It does not prove that an
assistant has loaded or followed them.

Start a new Claude Code or Codex conversation in a project outside this checkout
and ask:

```text
Without changing any files, inspect your loaded global instructions and tell me
which default engineering workflow they specify. Read its entrypoint and report
the exact file path. Tell me if you cannot access it.
```

Expect kw mode and a readable path inside the new checkout. If the agent cannot
launch a fresh session itself, leave this as an explicit user check and report
that runtime behavior remains unverified.

After that, just describe engineering tasks normally. `/kw-mode` in Claude Code
and `$kw-mode` in Codex remain available for explicit invocation. Casual chat
stays lightweight; “skip kw-mode for this task” opts out. These are instruction
defaults, subject to the runtime's instruction hierarchy and project guidance.

## Windows notes

The existing setup has been verified on macOS; native Windows installation is
not yet verified. Git may check out the `bin/setup` aliases as text files rather
than usable symlinks. In PowerShell, use the real entrypoint with a verified
Python 3.11+ interpreter, for example:

```powershell
py -3 --version
py -3 bin/kw.py doctor
py -3 bin/kw.py setup
py -3 bin/kw.py setup --apply
py -3 bin/kw.py doctor --installed --defaults
```

The installer also needs permission to create directory symlinks. Windows may
require Developer Mode or an elevated process; see
[Python's symlink documentation](https://docs.python.org/3/library/os.html#os.symlink).
Explain any required system change to the user. Verify the actual installation
and report any platform failure before claiming it works.

## Repairs and maintenance

| Symptom | Next step |
| --- | --- |
| Python cannot import `tomllib` | Use Python 3.11+ for every command. |
| Setup reports an existing path conflict | Inspect its target and contents; preserve it before any replacement. Never force-overwrite an unknown skill. |
| Default block markers are malformed or duplicated | Back up the instruction file, inspect the marked blocks, and repair only kw's block before rerunning setup. |
| Doctor passes but the assistant does not use kw mode | Start a fresh session; check the actual runtime home, loaded instructions, project overrides, and source readability. |
| A copied link points at the old computer | Identify it as a stale kw link, then replace that link through setup after preserving any real content. |
| A skill directory resolves into another Git checkout | Keep the personal link out of that checkout's commits; use a precise local `.git/info/exclude` entry if needed. |

To update a clean checkout from GitHub, run from its root:

```sh
git status --short
git pull --ff-only
python3 bin/kw.py doctor
python3 bin/kw.py setup --apply
python3 bin/kw.py doctor --installed --defaults
```

If there are local changes, preserve and reconcile them before pulling. Never
reset them just to update. Updates are pulled separately on each computer;
setup does not provide automatic cross-computer synchronization.

To relocate the checkout, remove its installation before moving it, then run
setup and doctor from the new location. To uninstall, run from the checkout:

```sh
python3 bin/kw.py setup --remove
python3 bin/kw.py setup --remove --apply
```

Removal deletes matching skill links and kw's managed default blocks while
preserving other instructions. It leaves the source checkout in place. Add the
same runtime flag if removing only one assistant's installation.

Edit [profile.md](../skills/kw-mode/profile.md) for preferences and
[runtime.md](../skills/kw-mode/runtime.md) for runtime guidance. Keep global
instructions as a short pointer to the skill so future updates have one source
of truth.

For ongoing upkeep, kw mode automatically checks when you start substantive work
and its seven-day interval is due. Ask “check pstack for useful updates to kw mode”
to check sooner. The [upstream review log](upstream-reviews.md) carries the last
completed check and pending ideas across computers when transferred with the
repository.
The check recommends selective changes; it does not automatically import them.
The ignored `.kw-state/` cache is machine-local and needs no migration. The first
session on a new computer checks again. Nothing runs while the assistants are
closed, and failed checks never block your engineering task.

Substantial implementation tasks automatically request an opposite-runtime review,
falling back to a fresh native reviewer when needed. The original agent fixes
confirmed findings and prepares commits. Install and sign in to both CLIs to make
cross-runtime review available; the main setup still works with one runtime.
The local `.kw-review/<task>/review.md` records feedback and resolutions. These
notes are excluded from Git; transfer active reviews separately when moving
computers. New tasks create their own handoffs.

## Completion report for the agent

Report the checkout path and revision, configured runtimes, resolved installation
paths, checks that passed or failed, and whether fresh-session loading was
verified. List only actual remaining user actions, such as login or starting a
new session. A setup request does not require a commit or push.
