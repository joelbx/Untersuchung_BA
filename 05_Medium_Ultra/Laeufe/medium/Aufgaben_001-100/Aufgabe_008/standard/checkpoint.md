Task: Add bounded reuse of known failed link fetches in Drive useLink.
Status: Implemented per-hook, per-(shareId, linkId) reuse for NOT_FOUND, NOT_ALLOWED, and INVALID_ID errors with 30-second expiry. Added tests for reuse, expiry, key isolation, non-cacheable errors, and successful responses.
Verification: Targeted useLink Jest suite passed (17 tests); Drive TypeScript check passed; git diff --check passed.
Constraints: Use local repository and existing tests; preserve git history and index baseline.
