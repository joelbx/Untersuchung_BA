Task: Fix email confirmation pending state, live TTL, expiry cleanup, and resend timing in /app.
Status: Implemented in src/user/email.js with a one-day default in install/data/defaults.json and focused regression tests in test/user/emails.js.
Verification: ESLint passed; email tests passed (11); broader user tests passed (259). Both test files were run separately against a temporary local Redis instance because they reset the same test database. The initial concurrent run of the user suite failed from database interference; its isolated rerun passed.
Final check: git diff --check and default JSON parse passed. Temporary Redis stopped.
