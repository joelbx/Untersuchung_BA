# Checkpoint

Task: Make `useDefaultShare` expose an awaitable `isShareAvailable(signal, shareId)` that checks locked and soft-deleted metadata while preserving default share behavior.

Completed: Added `isShareAvailable` using `useShare().getShare` and return value based on `isLocked` and `isVolumeSoftDeleted`. Added focused cases covering available, locked, and soft-deleted shares, including forwarding an `AbortController` signal.

Verification: `useDefaultShare.test.tsx` passed (6 tests). `git diff --check` passed.
