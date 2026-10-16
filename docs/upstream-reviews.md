# Upstream review log

Ask your agent: **“Check pstack for useful updates to kw mode.”**

The [review playbook](../skills/kw-mode/playbooks/upstream-review.md) compares new
upstream changes, checks whether they suit kw mode, and records decisions here.
kw mode automatically runs a due check at the first substantive task in a session,
fetching upstream at most weekly after successful checks. The standing preference
confirmed on 2026-10-16 authorizes automatic review and worthwhile local adoption,
verification, and a summary. No process runs between sessions. Task-specific
check-only, review-only, and read-only instructions override adoption. Commits and
publication remain separately scoped. Deferred work retains its reason and scope
here so the next substantive session can resume it.

This log records what has been reviewed. [upstream.json](../upstream.json) records
the sources actually imported. Keep both when moving computers so deferred ideas
and the next comparison baseline survive.

## Latest completed review

- Reviewed on: 2026-10-16 (UTC).
- Compared from: `f5bdd6826fd0a0d9cbc4347134c3a74a200b9d9d`.
- Reviewed through: `f713f14203cd6420cec13cd7c55c32d598dbab68`.
- Observed pstack version: `0.15.25`.
- Coverage: all 116 changed paths under `pstack/`, including added skills, scripts,
  tests, manifests, and guides. Full diff reviewed in three non-overlapping slices.
- Disposition: 22 source paths selectively adapted; 94 skipped with reasons below.
- Next suggested check: 2026-10-23. Explicit checks can run sooner.
- Imported changes: selective entry-level source commits and hashes in `upstream.json`;
  the original top-level imported baseline remains unchanged. `additional_sources`
  records supplementary source material without replacing a file's original source.
- Pending adoption or review candidates: none. The September uncertainty item is
  now incorporated in `workflows/writing.md`.

## 2026-10-16 decisions

Compared [prior reviewed snapshot](https://github.com/cursor/plugins/tree/f5bdd6826fd0a0d9cbc4347134c3a74a200b9d9d/pstack)
with [pinned snapshot](https://github.com/cursor/plugins/tree/f713f14203cd6420cec13cd7c55c32d598dbab68/pstack).
Upstream files were treated as source material; none of their setup, hooks, or
scripts were executed. Local paths in the table are relative to `skills/kw-mode/`.

The adopted changes improve premise testing, legitimate-state handling, retry
reconciliation, behavioral tests, benchmark/eval evidence, fresh-instance readiness,
state ownership, review pagination, worktree merge-target discovery, and status
and decision records. Cursor-specific machinery, hard-coded models, duplicated
commands, and removals of useful local safeguards were skipped. The automatic
adoption preference is a local user-directed change, not an upstream import.

| Upstream path | Decision | Reason and local target |
| --- | --- | --- |
| `pstack/skills/principle-attack-the-premise/SKILL.md` | Adapted | Replace actor-census-only reasoning and the unsupported claim that an even census disproves a premise with a discriminating test of the actual premise. Target same-name leaf and its index row. Avoid the upstream overclaim that any failed fix proves its premise false. |
| `pstack/skills/principle-build-the-lever/SKILL.md` | Skipped | Only formatting and prose compression; existing leaf carries same reasoning, no new behavior. Keep current target. |
| `pstack/skills/principle-encode-lessons-in-structure/SKILL.md` | Skipped | Removes nearly all rationale, strongest-mechanism guidance, and feedback routing. Local leaf remains useful independently and upstream's remaining fragment is insufficient as a replacement. |
| `pstack/skills/principle-exhaust-the-design-space/SKILL.md` | Skipped | Upstream reduces leaf to one context-dependent sentence, with trigger/rule carried in discovery frontmatter. Local reference leaves intentionally have no such frontmatter; retain current complete guidance. |
| `pstack/skills/principle-explain-the-number/SKILL.md` | Adapted | New useful evidence standard for performance and eval claims. Add same-name leaf and index row, route perf/eval/hillclimb to it. Preserve ability to report a measurement with explicit uncertainty when no limiter is established; do not claim diagnosis from a number alone. |
| `pstack/skills/principle-fix-root-causes/SKILL.md` | Adapted | Replace blanket ban on guards with legitimate-state versus invalid-state reasoning; add cheap diagnostic signal after a deep dig. Target same-name leaf/index. Preserve in-scope work, treat long comments as a clue rather than proof of wrong code, and do not wipe persistent state as a first diagnostic. |
| `pstack/skills/principle-guard-the-context-window/SKILL.md` | Skipped | Removes targeted reading/delegation/inline-content guidance. Local leaf deliberately conditions delegation on native runtime permission; preserve that adaptation. |
| `pstack/skills/principle-laziness-protocol/SKILL.md` | Skipped | Removes general simplification guidance with no new alternative mechanism. Existing local guidance remains appropriate; no import needed for removal alone. |
| `pstack/skills/principle-make-operations-idempotent/SKILL.md` | Adapted | Stronger state reconciliation and crash-evidence reasoning replaces unsafe reliance on PID-only stale-lock detection. Target same-name leaf. Preserve legitimate live state, and clarify idempotence is not a concurrency guarantee. |
| `pstack/skills/principle-migrate-callers-then-delete-legacy-apis/SKILL.md` | Skipped | Deletes most explanation/rules; local external compatibility exception and explicit internal migration sequence remain useful. |
| `pstack/skills/principle-minimize-reader-load/SKILL.md` | Skipped | Consolidates prose and headings only. Existing leaf already contains every substantive point. |
| `pstack/skills/principle-model-the-domain/SKILL.md` | Skipped | Shortens description and rationale, minor wording only; no new mechanism. Existing same-name leaf already covers all examples and anti-overabstraction boundary. |
| `pstack/skills/principle-never-block-on-the-human/SKILL.md` | Skipped | Formatting plus removes ambiguity guidance. Blind copy would lose local plan-only scope, unrelated-findings boundary, and reuse of prior authorization. Keep local same-name leaf. |
| `pstack/skills/principle-outcome-oriented-execution/SKILL.md` | Skipped | Only removes an explicit final-verification reminder. Existing leaf already scoped to planned reversible work; retain useful reminder. |
| `pstack/skills/principle-prove-it-works/SKILL.md` | Skipped | Removes actual-feature, end-to-end, and delegated-artifact checks. These remain useful local safeguards, including local conditional commit permission. |
| `pstack/skills/principle-redesign-from-first-principles/SKILL.md` | Skipped | Description shortening and synonymous opening sentence, no new behavior. |
| `pstack/skills/principle-sequence-verifiable-units/SKILL.md` | Skipped | Removes repeated pattern bullets; existing leaf is coherent and no functional change is needed. |
| `pstack/skills/principle-subtract-before-you-add/SKILL.md` | Skipped | Rationale/heading compression only; existing leaf covers same practice. |
| `pstack/skills/principle-test-behavior-not-implementation/SKILL.md` | Adapted | Fixes overspecified assertion-shape ban and undefined heuristic. Negative assertions and mocked external effects can be real contracts. Target same-name leaf/index; preserve legitimate error-text contracts, and avoid treating one hypothetical missed defect as proof an otherwise useful test proves nothing. |
| `pstack/skills/principle-type-system-discipline/SKILL.md` | Skipped | Removes constructive types, exhaustive matching, cast discipline, and concrete examples; local implementation does not carry these in another imported TS leaf. Keep local general-language guidance. |
| `pstack/skills/architect/SKILL.md` | Adapted | Add local-change safety to `workflows/architect.md`; skip Cursor role defaults and redundant compression. |
| `pstack/skills/architect/references/design-red-flags.md` | Adapted | One state owner, public boundaries, and derived registries add concrete design checks to `workflows/architect.md`; retain external-compatibility exception. |
| `pstack/skills/architect/references/runner-prompt.md` | Skipped | Only “several” to “parallel”; local arena already defines bounded native workers. |
| `pstack/skills/arena/SKILL.md` | Skipped | Primarily compression and Cursor model/fallback changes; local `workflows/arena.md` already has common contract, isolated outputs, independent judgment when available, synthesis, and re-verification. |
| `pstack/skills/automate-me/SKILL.md` | Skipped | Only job-based effort/speed assignment; no imported automate-me workflow, and kw inherits the current model through runtime/profile. |
| `pstack/skills/benchmark-checklist/SKILL.md` | Adapted | New valuable measurement validity workflow; target `workflows/benchmark.md` plus performance/hillclimb links, with platform-neutral tooling and proportionate trials. |
| `pstack/skills/blast-radius/SKILL.md` | Skipped | Mostly removes duplicated caution and changes model count wording; local `workflows/blast-radius.md` already proves the safety fact and identifies unproven risks. |
| `pstack/skills/correct/SKILL.md` | Adapted | Fold structural prevention and proof against real past mistakes into `workflows/reflect.md`; avoid redundant standalone skill and scope-expanding mandatory remediation. |
| `pstack/skills/create-verification-skill/SKILL.md` | Adapted | Usable readiness, faithful fresh-data journeys, and stand-in setup gaps improve `workflows/verify.md`. |
| `pstack/skills/figure-it-out/SKILL.md` | Skipped | Compression plus Cursor effort choice; local workflow already keeps bounded falsifiable experiments and verifies artifacts. Keep local lead ownership rather than removing artifact audit. |
| `pstack/skills/how/SKILL.md` | Skipped | Cursor-only role/default/fallback plumbing and compression; native local narrow-question direct exploration is intentional. |
| `pstack/skills/how/references/explorer-prompt.md` | Skipped | Deletes tracing instructions already represented by local `workflows/how.md`; retaining short entry-point and join checks is useful. |
| `pstack/skills/in-your-own-words/SKILL.md` | Skipped | New one-sentence command duplicates ordinary goal-restatement capability and existing figure-it-out/working-contract scope; no separate local installed command needed. |
| `pstack/skills/interrogate/SKILL.md` | Skipped | Mostly role-model changes and editorial reduction; local `workflows/review.md` already scopes intent, validates findings, and preserves review-only scope. |
| `pstack/skills/interrogate/references/code-quality-review.md` | Skipped | Removes anti-nit boilerplate; local review already prioritizes confirmed defects with concrete consequences. |
| `pstack/skills/interrogate/references/lead-judgment.md` | Skipped | Removes introduction and arbitrary five-item calibration; local review has neither numerical cap nor neutral-vote requirement. |
| `pstack/skills/interrogate/references/reviewer-prompt.md` | Skipped | Compression and removal of redundant cautions; keep local evidence-trigger-impact contract and intent challenge discipline. |
| `pstack/skills/interrogate/references/rubric.md` | Skipped | Editorial compression; correctness, boundary, concurrency, root-cause, and simplicity checks already exist locally. |
| `pstack/skills/ketchup/SKILL.md` | Adapted | Add brief evidence-based catch-up guidance to `workflows/writing.md`; retain local authorized-work continuity and avoid compulsory diagrams/format. |
| `pstack/skills/no-comments/SKILL.md` | Skipped | Cursor agent ID and effort update; local writing deliberately preserves useful rationale, public documentation, notices, and directives. |
| `pstack/skills/poteto-help/SKILL.md` | Skipped | New Cursor plugin/setup/menu map is not applicable to native kw; existing README/router document actual supported workflows. |
| `pstack/skills/poteto-help/references/prompting.md` | Skipped | Goal/done/evidence framing is already in local workflows; reject universal prototype mandates and advice that presumes Cursor loop behavior. |
| `pstack/skills/poteto-help/references/recipes.md` | Skipped | New examples primarily advertise Cursor slash commands absent from kw; no source change needed for existing natural-language routing. |
| `pstack/skills/recall/SKILL.md` | Skipped | Sole added effort/speed instruction conflicts with inherited-model preference; project-scoped recall is already maintained. |
| `pstack/skills/reflect/SKILL.md` | Skipped | Mostly compression/model plumbing; mandatory approval and automatic external backlog posting conflict with scoped authorization. Local reflection is already smaller. |
| `pstack/skills/reflect/references/divergent-reviewer.md` | Skipped | Mostly compression and removing arbitrary finding counts; local reflect has neither mandatory panels nor quotas and already requires evidence. |
| `pstack/skills/reflect/references/judgment-reviewer.md` | Skipped | Same compression/count cleanup; scoped local reflection already avoids speculative unrelated skill edits. |
| `pstack/skills/reflect/references/synthesizer.md` | Adapted | Explicitly read target and distinguish missing routing/weak placement from a missing rule; fold into `workflows/reflect.md` without separate synthesis prompt. |
| `pstack/skills/reflect/references/tooling-reviewer.md` | Skipped | Compression and quota removal; local evidence-based structural prevention already captures the useful behavior. |
| `pstack/skills/setup-pstack/SKILL.md` | Skipped | Cursor model-rule budget UI and hard-coded defaults; kw's Claude-first inherited runtime preferences remain authoritative. |
| `pstack/skills/sharpen/SKILL.md` | Skipped | New framing command overlaps figure-it-out, architect, and verify; automatic loosening of user constraints is unsuitable, and no additional local workflow earns its load. |
| `pstack/skills/show-me-your-work/SKILL.md` | Adapted | Preserve append-only correction, run attribution, and truthful evidence audits in local decision-log workflow. |
| `pstack/skills/show-me-your-work/scripts/log.sh` | Skipped | Upstream append header safety is sensible but kw has no imported helper and uses different TSV columns; prose append-only guidance covers current local mechanism. |
| `pstack/skills/swarm/SKILL.md` | Adapted | Pin revisions and measurement method in worker briefs/results; keep native tools and truthful coverage gaps. |
| `pstack/skills/tdd/SKILL.md` | Skipped | Removes nearby validation/redundant disclosure text; local TDD already small and nearby relevant checks remain valuable. |
| `pstack/skills/technical-writing/SKILL.md` | Skipped | Editorial pruning of a larger style catalog; local writing already short and preserves evidence/uncertainty. No new style mandates needed. |
| `pstack/skills/typescript-best-practices/references/patterns.md` | Adapted | Added schema-owned parsing and compiler-checked validator completeness to `principles/type-system-discipline.md`; no TypeScript-only dependency. |
| `pstack/skills/unslop/SKILL.md` | Skipped | Frontmatter fix and compression; local writing has no always-apply frontmatter bug and already keeps plain natural prose. |
| `pstack/skills/why/SKILL.md` | Skipped | Compression/role plumbing; local `workflows/why.md` deliberately searches only relevant records, not every available connector. |
| `pstack/skills/why/references/epistemics.md` | Skipped | Rephrases existing evidence tiers and uncertainty discipline; local why already separates intent, inference, and unknown. |
| `pstack/skills/why/references/investigator-prompt.md` | Skipped | Reorganizes existing evidence-gathering/contradiction rules; native local why already anchors claims and preserves gaps without extra prompt files. |
| `pstack/skills/why/references/sources/code-archaeology.md` | Skipped | Mostly removes examples/pitfalls; local history/blame/review search is already concise. |
| `pstack/skills/why/references/sources/datadog.md` | Skipped | Editorial compression of source-specific guide; kw does not import connector-specific search recipes. |
| `pstack/skills/why/references/sources/incident-postmortem.md` | Skipped | Trims source-specific incident hints; local why uses relevant in-scope evidence, without a mandatory multi-source sweep. |
| `pstack/skills/why/references/sources/sentry.md` | Skipped | Removes source explanation/pitfalls; no local Sentry-specific workflow and local uncertainty rules remain. |
| `pstack/skills/why/references/sources/slack.md` | Skipped | Removes explanatory sections and redundant thread guidance; no local Slack recipe; kw preserves scoped source access. |
| `pstack/skills/why/references/synthesizer-prompt.md` | Skipped | Compression preserves semantics already represented in local why; no separate prompt or fixed output schema needed. |
| `pstack/.cursor-plugin/plugin.json` | Skipped | Version discovery only; kw has its own installation and provenance. No local target. |
| `pstack/README.md` | Skipped | Guide/index/model/installation updates duplicate leaf material reviewed separately. Keep native kw instructions, automatic mode, and inherited models. Local README needs only descriptions of actually adopted behavior. |
| `pstack/agents/comment-sicko.md` | Skipped | Cursor agent identifier fix; no registered local agent counterpart. |
| `pstack/agents/poteto-agent.md` | Skipped | Lead-owned playbooks and absolute delegate reference paths already covered by `runtime.md`; Cursor discovery fallback and mandatory fresh-agent behavior do not fit native host contracts. |
| `pstack/docs/guide/01-setup.md` | Skipped | Cursor menus, model budgets, and setup-specific docs; kw inherits models and already installs automatic instructions. |
| `pstack/docs/guide/02-poteto-mode.md` | Skipped | Prompting examples and Cursor cloud/custom-mode operation. Local working contract already retains goal, acceptance, constraints, and resource isolation. |
| `pstack/docs/guide/03-understand.md` | Skipped | Read-only investigation and evidence are already explicit in `playbooks/investigation.md` and mode working contract. No guide import needed. |
| `pstack/docs/guide/04-design.md` | Skipped | Prototypes, caller-first design, and planning are already represented locally; consequential plan review remains valid and is not replaced with upstream's categorical prohibition. |
| `pstack/docs/guide/05-build-and-clean.md` | Skipped | New measurement guidance is handled from perf/hillclimb sources below; Cursor TypeScript invocation semantics do not apply. |
| `pstack/docs/guide/06-verify-and-ship.md` | Skipped | Measurement/readiness ideas are handled through leaf workflows; daily scheduling, universal control CLIs, and expanded guide are not required. |
| `pstack/docs/guide/07-overnight.md` | Skipped | Cloud Projects/automation pack absent locally. Native session persistence limits and explicit scope remain. Autopilot mechanics reviewed below. |
| `pstack/docs/guide/08-principles.md` | Skipped | Principle updates are covered by the principles review; do not create a duplicate guide. |
| `pstack/docs/guide/09-make-it-yours.md` | Skipped | Correct/reflect leaf workflows carry actionable ideas; Grok bot UI and Cursor authoring specifics have no local target. |
| `pstack/docs/guide/10-recipes-and-pitfalls.md` | Skipped | Summarizes other changed leaves; no independent local defect. |
| `pstack/docs/guide/README.md` | Skipped | Upstream guide navigation/count changes; no local counterpart. |
| `pstack/plugin.json` | Skipped | Agent Plugins v1 publishing manifest does not improve current shared-symlink installation. No plugin packaging migration requested. |
| `pstack/skills/poteto-mode/SKILL.md` | Adapted | Add the measurement-check workflow to the supporting index and route measured-number claims through it. Preserve local permission/scope contract, automatic activation, explicit local links, native delegation, model inheritance, and review handoff. Model slugs, universal fresh-agent rule, Cursor commands, and broad autonomy defaults skipped. Target `SKILL.md`. |
| `pstack/skills/poteto-mode/playbooks/autonomous-run.md` | Skipped | Only new subagent reasoning/speed routing; local model inheritance and host constraints remain. |
| `pstack/skills/poteto-mode/playbooks/autopilot-full.md` | Adapted | Keep durable ownership/head/evidence and distinguish meaningful progress from status claims. Verify changed behavior at the new head; retain unaffected evidence without mandatory full fanout on every fix. Do not copy fixed hourly loops, cloud store assumptions, immediate replacement before old writer stops, universal merge permission, or mandatory early publication. Target `playbooks/autopilot-full.md`. |
| `pstack/skills/poteto-mode/playbooks/autopilot-stack.md` | Adapted | Give topology changes a single owner in addition to one writer per branch; coordinate rebases/retargets and recheck affected evidence. Freeze unrelated topology edits while landing. Preserve separate landing scope. Target `playbooks/autopilot-stack.md`. |
| `pstack/skills/poteto-mode/playbooks/babysit.md` | Skipped | Owner/topology exceptions mostly belong to Cursor autopilot machinery. Local step 4 already refreshes exact-head state and step 6 keeps merging separately scoped. Pagination and human gate adaptation below comes from watcher source, not this diff. |
| `pstack/skills/poteto-mode/playbooks/bug-fix.md` | Skipped | Model default change and condensation. Local already reproduces, instruments, verifies, and owns diff; retain explicit independent review. |
| `pstack/skills/poteto-mode/playbooks/eval.md` | Skipped | Only model effort/speed instruction; preserve inherited models and controlled comparison. |
| `pstack/skills/poteto-mode/playbooks/feature.md` | Skipped | Model changes, removed duplication, mandatory delegation. Local narrower practical decomposition and lead review are appropriate. |
| `pstack/skills/poteto-mode/playbooks/hillclimb.md` | Adapted | Validate evaluator sensitivity and count errors/completed work before freezing; route performance to `workflows/benchmark.md`. No model pins or compulsory attempt floor. |
| `pstack/skills/poteto-mode/playbooks/multi-phase-plan.md` | Skipped | Ten lanes, model/loop configuration, rigid skeleton, and code-ready verification prescription are oversized for local plans; existing per-phase acceptance and scope suffice. |
| `pstack/skills/poteto-mode/playbooks/opening-a-pr.md` | Skipped | Native PR tool preference is already runtime guidance. Keep project templates, optional drafts, scoped publication, and concise descriptions over required Scope sections or universal ready PRs. |
| `pstack/skills/poteto-mode/playbooks/orchestrate.md` | Skipped | Graphite removal is useful upstream but local already has no forge/runtime dependency; retains native coordinator ownership. |
| `pstack/skills/poteto-mode/playbooks/pause-safely.md` | Skipped | Removal of contradictory clean-stop wording already matched locally by preserving partial/dirty work explicitly. |
| `pstack/skills/poteto-mode/playbooks/perf-issue.md` | Adapted | Linked baseline and later comparisons to `workflows/benchmark.md`; existing evidence-based optimization order retained. No model pins or mandatory strategy checklist. |
| `pstack/skills/poteto-mode/playbooks/refactoring.md` | Skipped | Model routing and duplicate ownership prose removal; local compact behavior/equivalence contract is stronger. |
| `pstack/skills/poteto-mode/playbooks/runtime-forensics.md` | Skipped | Only model effort/speed change. Native runtime and inheritance remain. |
| `pstack/skills/poteto-mode/playbooks/session-pickup.md` | Skipped | Only model effort/speed change. Preserve local reconciliation of historical claims against actual state. |
| `pstack/skills/poteto-mode/playbooks/shipping.md` | Skipped | Local already verifies independent evidence, contiguous stack, patch identity plus current integration checks, bottom-up landing, and readback. Upstream build-noise exception adds complexity and potentially weakens current proof. No change needed. |
| `pstack/skills/poteto-mode/playbooks/trace-forensics.md` | Skipped | Wording condensation and model settings; local causality/limitations contract already covers paired-capture uncertainty. |
| `pstack/skills/poteto-mode/playbooks/worktree-cleanup.md` | Adapted | Establish the actual merge target, including an explicit alternate target; do not assume main. Verify remote/default branch and evidence freshness. Preserve local untracked/dirty/active safeguards; do not import force cleanup or classify all untracked files as scratch. Target `playbooks/worktree-cleanup.md`. |
| `pstack/skills/poteto-mode/scripts/check-plan.mjs` | Skipped | Useful CommonMark fence fix belongs to an unimported rigid plan checker. kw has no corresponding parser. No local target. |
| `pstack/skills/poteto-mode/scripts/check-plan.test.ts` | Skipped | New fence cases test the absent checker; no local source to test. |
| `pstack/skills/poteto-mode/scripts/orch/orch.test.ts` | Skipped | Tests forge-backed chain discovery in absent orchestration runtime. Local uses native tools. |
| `pstack/skills/poteto-mode/scripts/orch/orch.ts` | Skipped | Graphite-to-forge options are unnecessary with no imported CLI. |
| `pstack/skills/poteto-mode/scripts/orch/store.ts` | Skipped | Forge chain resolver replaces Graphite, but importing a second runtime is unwarranted. Local topology ownership adapted in autopilot stack. Resolver uses local refs and assumes main if remote HEAD missing; do not copy those assumptions. |
| `pstack/skills/poteto-mode/scripts/package.json` | Skipped | Adds absent checker tests to absent Bun package. |
| `pstack/skills/poteto-mode/scripts/watch-pr/fakes.test-helper.ts` | Skipped | Fixtures for unimported watcher; pagination lesson covered by source below. |
| `pstack/skills/poteto-mode/scripts/watch-pr/github.test.ts` | Skipped | Read all pagination/gate test additions as evidence of intended semantics; no watcher to patch locally. |
| `pstack/skills/poteto-mode/scripts/watch-pr/github.ts` | Adapted | Native babysit must read all review-thread pages before reporting complete state and classify required human approval as a human gate, not retryable CI failure. Keep enforced approval intact; no TypeScript watcher import. Target `playbooks/babysit.md`. |
| `pstack/skills/poteto-mode/scripts/watch-pr/policy.test.ts` | Skipped | One expected-reader-call update for absent watcher. |
| `pstack/skills/poteto-mode/scripts/watch-pr/policy.ts` | Skipped | Integration call to pagination resolver; semantic adaptation covered by github.ts. |
| `pstack/skills/poteto-mode/scripts/watch-pr/types.ts` | Skipped | New raw/page types support absent watcher. |
| `pstack/skills/poteto-mode/scripts/worktree-audit.sh` | Skipped | Base-ref improvement is adapted through cleanup playbook. Script remains Cursor/transcript-specific, splits worktree paths on whitespace, and its safe bucket treats some closed/untracked work too permissively; do not import. |

## 2026-09-11 review

- Reviewed on: 2026-09-11 (UTC).
- Compared from: `27e2a62ff94f9af4b5e68435e41cdceacadb840c`.
- Reviewed through: `f5bdd6826fd0a0d9cbc4347134c3a74a200b9d9d`.
- Observed pstack version: `0.15.2`.
- Coverage: all five changed files under `pstack/`; two commits. No added,
  renamed, or deleted files in this comparison.
- Next suggested check: 2026-09-18. An explicit prompt can check sooner.
- Imported changes from this review: none.

## Decisions and pending ideas

| Upstream change | Decision | Reason and local target |
| --- | --- | --- |
| Evidence and uncertainty wording in the mode entrypoint ([source commit](https://github.com/cursor/plugins/commit/f8abeddd1862dc73704e3d719dd73df0d51b8c71)) | Adapted 2026-10-16 | Now makes the distinction between observed results, inference, and speculation explicit in `skills/kw-mode/workflows/writing.md`. kw already asks for evidence, but this would clarify how to state uncertainty. Avoid requiring a mechanical label on every sentence. |
| Neutral operator pronouns in the mode entrypoint and the three changed playbooks ([source commit](https://github.com/cursor/plugins/commit/f5bdd6826fd0a0d9cbc4347134c3a74a200b9d9d)) | Skip | kw's corresponding entrypoint, `autopilot-full.md`, `autopilot-stack.md`, and `multi-phase-plan.md` already use neutral wording. |
| In-chat status wording in upstream `multi-phase-plan.md` (same source commit) | Skip | kw's plan playbook has no copied status-tick mechanism. Its runtime contract already uses native session tools. No corresponding defect was found in the local file. |
| Cursor plugin manifest version change | Skip | kw has its own shared skill setup. A review does not advance the imported pstack version. |
