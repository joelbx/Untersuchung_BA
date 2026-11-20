Updated [useDefaultShare](/app/applications/drive/src/app/store/_shares/useDefaultShare.ts) to expose the awaitable `isShareAvailable(signal, shareId)`. It forwards both arguments to `getShare` and returns false for locked or soft-deleted shares. The existing default-share path is unchanged.

The focused Jest suite passed all 7 tests, including the existing volume-creation checks.