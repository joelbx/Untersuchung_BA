# Checkpoint

Implemented in `src/user/email.js`:
- Pending checks now validate both the per-user marker and matching confirmation record, and return strict booleans.
- Added `getValidationExpiry(uid)` using the store's live `pttl`, returning `null` when inactive and bounding the result to configured expiry.
- Added async `canSendValidation(uid, email)` using the remaining TTL, configured minute interval, and configured day expiry.
- Expiring a validation removes the marker and its associated record; new sends set both keys to the configured expiry.

Verification: `node --check` and ESLint pass. Existing `test/user/emails.js` could not run because its required Redis service is unavailable at `127.0.0.1:6379` (0 passing; setup hook failed).
