# Checkpoint

- Task: Make `useDefaultShare` report whether a share is available when its metadata is locked or soft-deleted.
- Repository: `/app`; working tree was clean at start.
- Located hook and tests under `applications/drive/src/app/store/_shares/`.
- Added `isShareAvailable(abortSignal, shareId)` to `useDefaultShare`; it forwards both arguments to `getShare` and rejects locked or soft-deleted metadata.
- `FolderContainer` now checks folder share availability and navigates to root when the share is unavailable.
- Added hook and folder-route regression tests. Both focused Jest suites passed (9 tests); ESLint, Prettier, and `git diff --check` passed.
- TypeScript check and final diff review passed. Work is complete.
