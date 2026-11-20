# Checkpoint

Task: Fix email confirmation pending state, live expiry TTL, expiration cleanup, and resend interval behavior in `src/user/email.js`.

Plan: Inspect existing code and tests, edit the repository, then run relevant existing tests. External research and downloads are excluded.

Status: Implemented a shared configurable expiry for both confirmation keys, live TTL lookup, strict pending state, resend eligibility, cleanup, and confirmation-code validation against the active marker. Added a one-day default, admin setting, and focused regression coverage.

Verification: Full `test/user.js` suite passed (256 tests); focused `test/user.js` suite passed (6 tests) after the final ownership check; `test/user/emails.js` passed (6 tests). ESLint, JSON parsing, and `git diff --check` passed. Tests used a disposable local Redis server.
