Updated [email.js](/app/src/user/email.js) so pending checks return a strict boolean, confirmation TTL comes from the store in milliseconds, expiry clears both records, and resend eligibility uses the configured interval. Added a one day default for `emailConfirmExpiry` in [defaults.json](/app/install/data/defaults.json).

ESLint passed, and all 254 tests in `test/user.js` passed.