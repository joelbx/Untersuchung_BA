# Checkpoint

Resolved: `useLink` now caches NOT_FOUND, NOT_ALLOWED, and INVALID_ID fetch errors per share/link pair for 5 seconds, then expires them. Other errors and successful links retain normal behavior.

Verification: focused Jest suite passed (17 tests); Drive TypeScript check passed; Prettier check and `git diff --check` passed.

Delegation: none.
