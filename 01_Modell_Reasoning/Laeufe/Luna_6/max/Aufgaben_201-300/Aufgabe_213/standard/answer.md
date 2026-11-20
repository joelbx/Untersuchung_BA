Implemented `isShareAvailable(signal, shareId)` in [useDefaultShare.ts](/app/applications/drive/src/app/store/_shares/useDefaultShare.ts:23). It awaits `getShare` with the provided signal and returns `false` for locked or soft-deleted shares.

Added coverage for availability, both unavailable states, and signal forwarding in [useDefaultShare.test.tsx](/app/applications/drive/src/app/store/_shares/useDefaultShare.test.tsx:125). The existing default-share creation checks still pass.

**Verification:** focused Jest suite passed (6 tests); `git diff --check` is clean.