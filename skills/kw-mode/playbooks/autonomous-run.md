# Autonomous run

1. State a falsifiable completion condition, scope, constraints, and any user-set
   resource budget. Keep that condition fixed unless the user changes it.
2. Choose the appropriate narrow playbook for the next unit. Establish its baseline
   and verification before changing the artifact.
3. Execute one useful unit and check it. Keep improvements, remove unsuccessful
   task-owned experiments, and resolve in-scope blockers without unnecessary pauses.
4. Keep a [decision trail](../workflows/show-me-your-work.md). Checkpoint the current
   artifact, observations, and next step after meaningful progress.
5. Use the host's actual wait or loop facilities for external events. Do not claim
   background execution after the session ends. Stay within granted permissions;
   unattended work does not authorize unrelated posting, deployment, or deletion.
6. Continue until the completion condition, explicit stop, budget, or genuine blocker.
   At a plateau, change the hypothesis rather than repeat the same failed attempt.
   If stopping incomplete, use [pause safely](pause-safely.md).

Reply with the completion condition, final evidence, accepted/discarded work, and status.
