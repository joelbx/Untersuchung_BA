`useDefaultShare` now exposes awaitable `isShareAvailable(signal, shareId)`. It forwards the signal to `getShare` and returns `false` for locked or soft-deleted shares. The default-share loading path is unchanged.

All seven hook tests pass, including the existing single-volume-creation cases. Drive type checking and formatting checks also pass.