# Checkpoint

Task: Add bounded reuse of known API fetch errors in Drive `useLink`, scoped to each share and link pair, then run relevant existing tests.

Status: Implemented 30-second reuse of NOT_FOUND, NOT_ALLOWED, and INVALID_ID API errors by share/link pair. Added focused tests for reuse, expiry, isolation, successful fetches, and uncached errors.

Verification: Existing `useLink.test.ts` and new `useLink.fetchErrors.test.ts` passed (17 tests). Focused new suite passed after the final test refinement (5 tests). ESLint passed for both edited source files.
