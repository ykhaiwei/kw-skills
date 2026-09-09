# Worktree cleanup

1. Inventory candidates and their size, repository, branch, dirty state, upstream
   relationship, unmerged commits, and active task/process ownership.
2. Establish which resources are actually disposable within the cleanup request.
   Preserve dirty, untracked, unmerged, active, or uncertain work. A branch name or
   age alone does not prove a worktree is abandoned.
3. Present the concrete candidate list and perform only authorized removals using
   the owning tool. Do not use force flags to bypass unresolved ownership or data.
4. Stop only processes demonstrably owned by the discarded task. Leave shared
   development services and unrelated simulators or caches alone.
5. Recheck worktree metadata and disk use. Report removed resources, recovered
   space, preserved candidates, and reasons for any unresolved items.
