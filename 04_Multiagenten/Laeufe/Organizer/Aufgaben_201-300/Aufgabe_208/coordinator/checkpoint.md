Task: Fix email confirmation pending state, live TTL, expiry cleanup, and resend timing in /app.
Status: Complete. Implemented strict pending state, live TTL, resend interval, shared expiry, cleanup, and stale-link rejection. Added regression coverage. Full test/user.js passed (255 tests); after final assertions, focused email confirmation suite passed (5 tests). ESLint and git diff --check passed. Local temporary Redis stopped.
Constraints: Local code and tests only; preserve git history, index, and harness configuration.
