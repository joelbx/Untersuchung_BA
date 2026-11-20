Added `isShareAvailable(abortSignal, shareId)` to `useDefaultShare`. It calls `getShare` with the supplied signal and returns `false` for locked or soft-deleted shares. Default share loading and volume creation remain unchanged.

The hook test now covers available and unavailable metadata, signal forwarding, and existing default share behavior. All 4 tests passed.