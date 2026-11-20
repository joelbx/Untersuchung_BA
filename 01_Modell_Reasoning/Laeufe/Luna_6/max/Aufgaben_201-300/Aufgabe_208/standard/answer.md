Implemented the confirmation state, TTL, and resend fixes in [email.js](/app/src/user/email.js). Pending checks now return strict booleans, match the optional email, and clear expired records. The new `getValidationExpiry` and `canSendValidation` APIs use the store’s live TTL and the configured interval.

Confirmation records and user markers now share the configured expiry. Added a one day default and an admin setting in [defaults.json](/app/install/data/defaults.json), [user.tpl](/app/src/views/admin/settings/user.tpl), and [user.json](/app/public/language/en-GB/admin/settings/user.json).

**Validation:** `test/user/emails.js` passed (6 tests). ESLint, syntax, JSON, and diff checks passed. The test suite logged a sendmail warning, but all tests passed.