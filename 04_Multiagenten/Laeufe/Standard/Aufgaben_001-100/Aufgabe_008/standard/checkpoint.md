Task: Add short-lived per-(shareId, linkId) reuse for known fetchLink failures in Drive useLink.
Status: Complete. Implemented a 10-second error cache for NOT_FOUND, NOT_ALLOWED, and INVALID_ID with per-pair isolation. Focused Jest suite passed (17 tests); ESLint, Prettier, and git diff --check passed.
