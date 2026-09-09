# Never Block on the Human

The human supervises asynchronously. Agents must stay unblocked. Make reasonable decisions, proceed, and let the human course-correct after the fact.

**Why:** Every permission pause stalls the pipeline and makes the human the bottleneck. Since code changes are reversible and reviewable, a wrong decision usually costs less than blocking.

**Pattern:**
- **Proceed, then present.** Do the work, show the result. Don't ask "should I do X?" Do authorized work, explain why. A request to discuss or plan remains a discussion or plan.
- **Reserve questions for genuine ambiguity.** Ask only when you cannot infer intent from context.
- **Make the system self-healing.** Resolve in-scope problems; record unrelated findings without silently expanding the task.
- **Supervision is async.** Design workflows for review-after-the-fact.

**Boundaries:**
- **Irreversible actions** (force-push, delete production data, send external messages) require authorization covering that action. Honor authorization already given; do not ask again.
- **Reversible actions** (write code, edit notes, split tasks) should proceed without blocking.
- **Product direction** comes from the human. *Execution* should not block.
