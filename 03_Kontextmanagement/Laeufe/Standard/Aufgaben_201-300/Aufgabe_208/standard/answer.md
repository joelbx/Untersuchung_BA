Updated [email confirmation handling](/app/src/user/email.js) to return a strict pending state and a live TTL in milliseconds, enforce the configured resend interval, clear confirmations on expiry, and reject old codes. Added a one-day default expiry and a regression test.

Verification: 5 focused confirmation tests and 6 email API tests passed; ESLint and `git diff --check` passed.