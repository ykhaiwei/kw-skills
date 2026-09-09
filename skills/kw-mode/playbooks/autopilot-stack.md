# Autopilot stack

1. Define the target behavior and a sequence of independently verifiable changes.
   Record which branch depends on which predecessor.
2. Build the root against the actual trunk and each child against its parent's
   current tip. Use one owner per writable branch and follow repository conventions.
3. Verify each slice before building the next. Use [sequence verifiable units](../principles/sequence-verifiable-units.md)
   and keep the acceptance evidence attached to the tested base/head.
4. Open authorized reviews with each child targeting its parent. After upstream
   edits, update descendants carefully and rerun affected integration checks.
5. Verify the aggregate stack and report the bottom-to-top dependency list, review
   links where present, and evidence. This playbook delivers the stack for landing;
   merge only when separately covered by the request through [shipping](shipping.md).
