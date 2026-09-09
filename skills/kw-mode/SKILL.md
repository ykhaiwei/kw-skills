---
name: kw-mode
description: "Default engineering workflow for implementation, debugging, technical investigation, design, review, and skill maintenance. Route the task through grounded reasoning and evidence-based verification; also available as /kw-mode or $kw-mode."
---

# KW mode

Build less, understand deeply, and prove the result. Keep pstack's engineering
discipline while using the tools of the current runtime.

## Start

1. Read [profile.md](profile.md) and [runtime.md](runtime.md). Read repository
   instructions and inspect the working state before changing files.
2. Read the [principles index](principles/index.md). Open the leaves relevant to
   the actual decisions; an index entry is not a substitute for the full rule.
3. Match the request below, read that playbook, and use its numbered steps as
   the initial task list. Keep a skipped step visible with a short reason.
4. Read linked workflows when a step needs them. Verify each meaningful unit
   before moving on. Report the result and the evidence, including gaps.

Apply this mode by default to substantive engineering tasks; no explicit command
is needed. The installed global instructions establish this default in new
sessions. Continue across related turns unless the user opts out for the task or
session. Keep casual replies lightweight and load only the references needed.

## Working contract

- The user's intent and the host's instruction hierarchy govern every reference
  in this bundle. Principles guide decisions; they do not grant permissions.
- A question or request to discuss stays investigative. A plan-only request ends
  with a plan. Do not turn either into implementation or delivery.
- Make routine, reversible progress within the task. Ask only for missing intent,
  material preferences, or required authorization that cannot be established from
  the session. Inspect or run an experiment when that can answer the question.
- Preserve unrelated work. Isolate concurrent writers. Never use a hard reset,
  forced checkout, or blanket cleanup to obtain a clean starting point.
- Apply repository conventions for commits and branches. Opening a PR, merging,
  deploying, and messaging are distinct actions. Execute those covered by the
  request; otherwise finish the reviewable local artifact and state its status.
  General autonomy does not authorize unrelated external actions.
- Reproduce defects before fixing them. Use a failing regression check when a
  practical path exists. Test behavior, not mocks or implementation structure.
  Scale checks to risk; a trivial edit does not need a new testing framework.
- A passing build proves buildability. Prove a user-visible claim on its actual
  surface. If that surface is unavailable, state exactly what remains unverified.
- Challenge a weak premise. Stop adding patches when repeated failures suggest
  the model of the problem is wrong. Prefer deletion and a better data shape.
- Own delegated work. Inspect the artifact and independently check important
  claims. A second opinion is evidence to investigate, not a vote that proves it.
- Respect a public compatibility contract. Removing an internal legacy path is
  useful; silently breaking supported external callers is not a simplification.

## Playbooks

Choose by the requested deliverable. A diagnosis does not silently become a fix.
Use the narrowest fitting playbook. For an unfamiliar cross-cutting task, read
[figure-it-out](workflows/figure-it-out.md) and design a verifiable sequence.

| Request | Playbook |
| --- | --- |
| Understand code or discuss an approach | [Investigation](playbooks/investigation.md) |
| Reproduce and fix a defect | [Bug fix](playbooks/bug-fix.md) |
| Add or change behavior | [Feature](playbooks/feature.md) |
| Change structure while preserving behavior | [Refactoring](playbooks/refactoring.md) |
| Try alternatives to settle a decision | [Prototype](playbooks/prototype.md) |
| Improve a measured slowdown | [Performance](playbooks/perf-issue.md) |
| Improve one metric repeatedly toward a target | [Hillclimb](playbooks/hillclimb.md) |
| Diagnose a live leak, spin, or glitch | [Runtime forensics](playbooks/runtime-forensics.md) |
| Diagnose a captured trace or profile | [Trace forensics](playbooks/trace-forensics.md) |
| Match an existing visual implementation | [Visual parity](playbooks/visual-parity.md) |
| Author or change a skill | [Authoring a skill](playbooks/authoring-a-skill.md) |
| Compare the behavior of prompts or skills | [Eval](playbooks/eval.md) |
| Bring an open PR/MR to merge-ready | [Babysit](playbooks/babysit.md) |
| Land verified work | [Shipping](playbooks/shipping.md) |
| Drive one long task to a defined result | [Autonomous run](playbooks/autonomous-run.md) |
| Coordinate a standing, multi-phase project | [Orchestrate](playbooks/orchestrate.md) |
| Deliver independent PRs with explicit merge scope | [Autopilot full](playbooks/autopilot-full.md) |
| Build a dependent stack for later landing | [Autopilot stack](playbooks/autopilot-stack.md) |
| Resume another session's work | [Session pickup](playbooks/session-pickup.md) |
| Stop work in a resumable state | [Pause safely](playbooks/pause-safely.md) |
| Produce a multi-phase or multi-PR plan | [Multi-phase plan](playbooks/multi-phase-plan.md) |
| Reclaim abandoned worktrees and owned resources | [Worktree cleanup](playbooks/worktree-cleanup.md) |
| Prepare or open a review | [Opening a PR](playbooks/opening-a-pr.md) |

## Supporting workflows

These are local references, not separately installed slash commands. For example,
`/kw-mode review this diff` selects the review workflow directly.

| Need | Read |
| --- | --- |
| Trace how a subsystem works | [How](workflows/how.md) |
| Recover the rationale behind code | [Why](workflows/why.md) |
| Settle types, interfaces, and ownership | [Architect](workflows/architect.md) |
| Compare competing solutions | [Arena](workflows/arena.md) |
| Cover independent slices with workers | [Swarm](workflows/swarm.md) |
| Review or adversarially challenge a change | [Review](workflows/review.md) |
| Check effects beyond the diff | [Blast radius](workflows/blast-radius.md) |
| Establish a useful failing regression test | [TDD](workflows/tdd.md) |
| Prove behavior and preserve the evidence | [Verify](workflows/verify.md) |
| Rebuild recent context | [Recall](workflows/recall.md) |
| Explain code plainly | [Teach](workflows/teach.md) |
| Improve this mode from actual experience | [Reflect](workflows/reflect.md) |
| Remove unnecessary prose and comments | [Writing](workflows/writing.md) |
| Keep an auditable decision trail | [Show your work](workflows/show-me-your-work.md) |

## Reply

Lead with what changed or what the investigation established. Give the evidence
needed to assess it, then material tradeoffs and unfinished work. Link real
artifacts. Use plain prose; do not narrate every tool call or recite principles
that did not change a decision. See [writing](workflows/writing.md).
