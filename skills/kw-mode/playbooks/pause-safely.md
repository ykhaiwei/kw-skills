# Pause safely

1. Stop launching new work. Identify active workers, owned processes, and changes
   still in flight. Cancel or settle them using the host's actual controls.
2. Preserve all completed and partial work without destructive cleanup. Record
   dirty files and uncommitted changes rather than invent a clean state.
3. Write a concise handoff containing goal, constraints, decisions, artifact and
   branch paths, tested revisions, evidence, blockers, and the exact next step.
4. Record which processes remain alive and how to resume or stop owned resources.
   Do not stop shared services merely because the current task is pausing.
5. Give the user the handoff path and precise completion status. Resume later via
   [session pickup](session-pickup.md).
