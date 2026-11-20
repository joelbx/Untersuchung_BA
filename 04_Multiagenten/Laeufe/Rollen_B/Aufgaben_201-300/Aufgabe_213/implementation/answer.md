Added `isShareAvailable(abortSignal, shareId)` to `useDefaultShare`. It forwards the signal to `getShare` and returns `false` for locked or soft-deleted shares. Folder routes now return to the root when their share is unavailable.

The targeted tests pass, including the existing default-share creation checks. ESLint and the Drive TypeScript check also pass.