Task: Fix mailbox list loading around pending backend actions, request failures, and stale responses.
Status: Complete. Added backend action tracking to item operation hooks, guarded list reloads and in-flight results, propagated Stale and added separate timed retry paths, and updated loading selection. Mailbox.elements (12 tests) and Mailbox.labels (8 tests) passed; mail TypeScript check passed; git diff --check passed.
Constraints: Local repository and existing tests only; preserved git history, index baseline, and harness configuration.
