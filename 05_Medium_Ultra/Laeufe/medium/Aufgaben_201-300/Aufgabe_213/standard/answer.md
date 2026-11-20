`useDefaultShare` now exposes `isShareAvailable(signal, shareId)`. It forwards both arguments to `getShare` and returns `false` when the share is locked or soft-deleted. The default-share loading path is unchanged.

The focused Jest suite passed all 7 tests, including the existing volume-creation tests. Formatting and diff checks also passed.