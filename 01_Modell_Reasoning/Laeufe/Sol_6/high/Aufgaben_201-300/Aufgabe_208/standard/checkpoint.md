# Email confirmation fix

- Task: make pending state, live TTL, expiry cleanup, and resend timing consistent.
- Status: implemented and verified.
- Changes: added configurable one-day default expiry; kept marker and confirmation record on one deadline; added live TTL and resend eligibility helpers; made pending state boolean and email-specific; rejected orphaned confirmation codes; added regression coverage.
- Verification: `mocha test/user.js --grep '^User email confirm '` (5 passing), `mocha test/user/emails.js` (6 passing), ESLint and `git diff --check` passed.
