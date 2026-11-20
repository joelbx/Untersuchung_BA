Task: implement registration token interactive auth for stable and unstable Matrix stage types.
Status: complete. Added token entry view, stage routing, and focused tests for both stage types, submission, busy/error states, and completion callback.
Verification: focused Jest suite passed (4 tests); ESLint passed; Prettier applied. Full tsc --noEmit reports unrelated existing Sliding Sync type errors; no errors in changed files.
