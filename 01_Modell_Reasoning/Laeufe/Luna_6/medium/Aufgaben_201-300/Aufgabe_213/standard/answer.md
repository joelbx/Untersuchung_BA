Added `isShareAvailable(abortSignal, shareId)` to `useDefaultShare`. It calls `getShare` with both arguments and returns `false` for locked or soft-deleted shares.

Added coverage for availability results and `AbortController` signal forwarding. The existing default-share logic is unchanged.

Prettier and `git diff --check` passed. The focused Jest run did not complete: both workspace and direct invocations stalled without output, so I stopped them.