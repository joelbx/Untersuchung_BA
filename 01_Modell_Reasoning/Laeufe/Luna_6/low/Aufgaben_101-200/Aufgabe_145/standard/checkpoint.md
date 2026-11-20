# Checkpoint

Implemented photo recovery enumeration and recovery changes.

- Added an opt-in listing helper that loads regular children and, when requested, trashed links for the provided volume. The existing `loadChildren` default behavior is unchanged.
- Recovery waits until regular and trashed links finish decrypting, merges regular links with trashed image files, and counts the combined set.
- Share cleanup now checks for remaining photo files in both sources. Core action errors transition the persisted recovery state to failed; thrown move failures update the failed count.
- Existing in-progress persisted state continues to start recovery automatically.

Verification: `yarn workspace @proton/drive-store test --runInBand store/_photos/usePhotosRecovery.test.ts` passes (7 tests). The workspace type check previously reported a pre-existing crypto type incompatibility; its first run also caught and led to fixing a listing helper typing issue.
