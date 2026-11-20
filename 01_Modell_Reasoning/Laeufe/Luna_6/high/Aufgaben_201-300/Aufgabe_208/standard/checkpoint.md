# Email confirmation expiry and resend

- Updated `src/user/email.js` so pending checks return strict booleans and optionally match the stored confirmation email.
- Added live store TTL reporting and resend eligibility using configured expiry in days and interval in minutes, converted to milliseconds.
- Confirmation marker and record now share the configured expiry; explicit expiration deletes the marker and its corresponding record.
- `npx eslint src/user/email.js` and `git diff --check` pass.
- `npx mocha test/user/emails.js` could not run because Redis at `127.0.0.1:6379` is unavailable (`ECONNREFUSED`).
