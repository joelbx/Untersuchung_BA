# Checkpoint

Implemented mark-as status propagation, `OptimisticUpdates.markAsStatus`, and the bypass helper/reducer flow. When the active unread filter matches the requested mark status, affected IDs are removed from `bypassFilter`; otherwise they are added.

Verification: the existing `elementTotal.test.ts` passed. Mailbox element tests and TypeScript checking were started but did not produce completion output during this run. `git diff --check` passed.
