Task: Resolve PosthogAnalytics initialization, privacy state, tracking, room hashing, redaction, and logout behavior.
Status: Complete. Updated src/PosthogAnalytics.ts and test/PosthogAnalytics-test.ts.
Verification: Focused Jest suite passed (17 tests); ESLint passed on both touched files; git diff --check passed. Full TypeScript check still has unrelated existing repository/dependency errors; no PosthogAnalytics diagnostics appeared.
