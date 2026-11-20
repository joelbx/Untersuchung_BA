Added `isShareAvailable(signal, shareId)` to [useDefaultShare.ts](/app/applications/drive/src/app/store/_shares/useDefaultShare.ts). It forwards the signal to `getShare` and returns `false` for locked or soft-deleted shares.

The focused test suite passed: 6 tests, including the existing default-share creation checks.