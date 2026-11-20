# Checkpoint

Issue: `useDefaultShare` must expose an abortable availability check for a share, while preserving default-share loading/creation behavior.

Implemented:
- Added `isShareAvailable(abortSignal, shareId)` using `getShare` and the `isLocked` / `isVolumeSoftDeleted` flags.
- Folder routes now navigate to the root when their share is unavailable.
- The default-share loading and volume creation path is unchanged.

Verification: `yarn workspace proton-drive test --runTestsByPath src/app/store/_shares/useDefaultShare.test.tsx` passed (3 tests). `git diff --check` passed.
