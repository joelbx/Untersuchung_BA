# Checkpoint

- Located `useDefaultShare` and its existing tests in `applications/drive/src/app/store/_shares`.
- Added `isShareAvailable(signal, shareId)` using `getShare` and both metadata flags.
- Folder routes now redirect to root when the share is locked or soft-deleted.
- Added four metadata combinations to the existing hook tests.
- Verification passed: focused Jest suite (7 tests), Drive TypeScript check, Prettier check, and `git diff --check`.
