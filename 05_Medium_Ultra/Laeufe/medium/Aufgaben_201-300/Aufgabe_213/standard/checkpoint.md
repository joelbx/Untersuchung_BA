# Checkpoint

Task: Fix folder loading when a share is locked or soft-deleted.
Completed: `useDefaultShare` exposes `isShareAvailable(signal, shareId)`, forwards both arguments to `getShare`, and reports unavailable for locked or soft-deleted shares. Existing default-share behavior is unchanged.
Validation: Focused Jest suite passed (7 tests); Prettier and `git diff --check` passed.
