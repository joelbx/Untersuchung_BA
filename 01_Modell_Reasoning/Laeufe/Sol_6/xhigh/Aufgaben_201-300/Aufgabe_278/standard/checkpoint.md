# Checkpoint

Task: Resolve mailbox list reload timing, failed request retries, stale response handling, and loading state.

Implemented: Added pending backend action state/actions and deferred list resets, requests, and search updates until the counter returns to zero. Tracked label, move, mark, delete, and empty-label operations through event updates, waiting for every label request in a batch. Rejected stale responses and scheduled one-second stale retries; scheduled two-second failure retries and registered both reducers. Updated loading selector with current page and params and discarded query results that arrive during backend activity.

Verification: Mail TypeScript check, ESLint, Prettier, and git diff check passed. Mailbox elements and focused elements tests passed together (16 tests). Existing mailbox labels suite passed (8 tests). Targeted cache reset deferral integration test passed.

Status: Complete.
