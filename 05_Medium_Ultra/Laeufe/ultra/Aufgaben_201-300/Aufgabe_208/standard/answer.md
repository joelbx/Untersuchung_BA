Resolved the email confirmation expiry and resend issue. Pending checks now return strict booleans, `getValidationExpiry` returns the live remaining TTL in milliseconds or `null`, and `canSendValidation` applies the configured resend interval. Expiring a confirmation clears both keys; the marker and link now share the configured expiry. Old links are rejected after their pending marker expires.

Added a one-day default in [defaults.json](/app/install/data/defaults.json:149) and regression coverage in [emails.js](/app/test/user/emails.js:111). The implementation is in [email.js](/app/src/user/email.js:47).

The focused email tests, broader user tests, ESLint, and diff checks passed. I delegated test coverage and store TTL review, then integrated and verified the patch.