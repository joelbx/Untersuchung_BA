Added `isShareAvailable(signal, shareId)` to [useDefaultShare.ts](/app/applications/drive/src/app/store/_shares/useDefaultShare.ts). It forwards the signal to `getShare` and returns `false` for locked or soft-deleted shares. The default share loading path is unchanged.

The focused tests passed: 7 tests covering availability, signal forwarding, and default share creation.