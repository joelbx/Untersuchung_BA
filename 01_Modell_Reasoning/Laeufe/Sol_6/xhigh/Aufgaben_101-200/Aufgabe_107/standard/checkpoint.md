# Checkpoint

Task complete: stale optimistic mark-as bypass IDs are removed when the active read/unread filter matches the new status.

Changes: dispatch includes markAsStatus; OptimisticUpdates declares it; getElementsToBypassFilter classifies elements; reducer adds or removes derived message/conversation IDs. Focused reducer tests cover both filter values and conversation mode.

Verification: reducer and existing elementTotal Jest suites passed (8 tests), targeted ESLint passed, Prettier passed, mail TypeScript check passed, and git diff --check passed.
