# Checkpoint

Implemented the confirmation key refactor and ACP email status behavior.

- Added `confirm:byUid:<uid>` mappings and explicit millisecond `expires` fields in `confirm:<code>` objects.
- Added email fallback, pending-state, and expiry utilities; resend rejects an active pending confirmation unless forced.
- ACP user rows now show Validated, Validation Pending, Validation Expired, or (no email), with pending confirmation email fallback.
- Confirmation by code now validates expiry and correctly confirms when the email already matches; ACP confirmation can recover an email from pending data.
- User deletion removes the UID mapping and its associated confirmation object.

Verification: ESLint and `git diff --check` pass. `mocha test/user.js test/controllers-admin.js` was attempted but could not start because Redis at `127.0.0.1:6379` refused the connection.
