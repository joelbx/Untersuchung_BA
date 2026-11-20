Implemented the mailbox list loading and retry changes. Loads now wait until `pendingActions` reaches zero; loading reflects the current request context; and stale responses trigger a targeted retry without being committed.

Added the exported backend lifecycle actions, reducer cases, and `pendingActions` state. Generic failures retry after 2 seconds, while stale responses retry after 1 second.

Validation: `yarn workspace proton-mail check-types` passed. The repository changes are in the checked-out files, with a checkpoint at [.codex-role-output/checkpoint.md](/app/.codex-role-output/checkpoint.md).