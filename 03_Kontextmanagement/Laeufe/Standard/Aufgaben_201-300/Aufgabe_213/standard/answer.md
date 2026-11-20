Added `isShareAvailable(signal, shareId)` to [useDefaultShare.ts](/app/applications/drive/src/app/store/_shares/useDefaultShare.ts). It forwards the signal to `getShare` and returns `false` for locked or soft-deleted shares. The default-share loading path is unchanged.

The targeted Jest suite passed: 6 tests, including the existing volume-creation checks and new availability checks.