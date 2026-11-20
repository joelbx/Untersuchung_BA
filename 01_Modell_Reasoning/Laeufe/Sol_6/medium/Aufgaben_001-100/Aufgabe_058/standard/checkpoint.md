Task: Resolve PosthogAnalytics initialization, privacy, and tracking behavior.
Status: Implemented enum anonymity, DNT enforcement, config validation, enabled and initialised states, guarded awaited capture, identification and room hashing, URL redaction, and logout. Updated focused tests.
Verification: PosthogAnalytics Jest suite passes (17 tests); focused ESLint and git diff --check pass. Full TypeScript check remains blocked by pre-existing errors elsewhere in the repository and dependency typings.
