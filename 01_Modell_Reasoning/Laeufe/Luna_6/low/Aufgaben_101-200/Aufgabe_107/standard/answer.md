Implemented the bypass filter update. Mark-as dispatches now include `markAsStatus`; the reducer uses the active unread filter to add IDs that need bypassing or remove IDs that no longer do.

The existing `elementTotal.test.ts` passed, and `git diff --check` passed. Mailbox element tests and TypeScript checking did not finish during this run.