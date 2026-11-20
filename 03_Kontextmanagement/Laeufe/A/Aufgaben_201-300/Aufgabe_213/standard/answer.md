Added `isShareAvailable(signal, shareId)` to [useDefaultShare](/app/applications/drive/src/app/store/_shares/useDefaultShare.ts). It forwards the signal to `getShare` and returns `false` for locked or soft-deleted shares.

The focused suite passed all 6 tests, including the existing default-share creation tests.