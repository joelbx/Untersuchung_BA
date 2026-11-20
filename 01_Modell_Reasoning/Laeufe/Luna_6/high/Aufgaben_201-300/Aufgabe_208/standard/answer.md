Implemented the email confirmation expiry and resend fix in [src/user/email.js](/app/src/user/email.js).

Pending checks now return strict booleans and can match an email. Added `getValidationExpiry` using the store’s live TTL and `canSendValidation` using the configured day and minute units. Confirmation markers and records now expire after the configured lifetime, and explicit expiry clears both.

`npx eslint src/user/email.js` and `git diff --check` pass. The existing email test could not run because Redis at `127.0.0.1:6379` refused the connection.