Task: Fix email confirmation pending state, live TTL, expiry cleanup, and resend eligibility.
Status: Complete. Added configured one-day expiry, live millisecond TTL API, resend interval check, strict pending state, synchronized confirmation record expiry, and orphan-code rejection. Added regression test.
Verification: test/user.js 255 passing; test/user/emails.js 6 passing; ESLint and git diff --check passed.
