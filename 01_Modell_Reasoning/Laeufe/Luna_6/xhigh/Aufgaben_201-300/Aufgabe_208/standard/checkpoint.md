# Checkpoint

Resolved email confirmation expiry and resend handling in `/app`.

Implementation:
- Added a one-day default `emailConfirmExpiry` setting, preserving the prior hard-coded link lifetime.
- Set the per-user pending marker and confirmation record to the same configured expiry deadline.
- Added `UserEmail.getValidationExpiry(uid)` using the confirmation record's live database TTL in milliseconds, bounded to the configured expiry.
- Added `UserEmail.canSendValidation(uid, email)` using the awaited, email-aware pending check and the required TTL/interval/expiry comparison.
- Made pending checks return strict booleans and verify the record belongs to the user and is still live.
- Made explicit expiry delete the per-user marker and linked confirmation record.

Verification:
- `npx eslint src/user/email.js` passed.
- `git diff --check` passed.
- Focused existing email confirmation tests passed: 12 passing. The local test Redis instance was stopped after the run.
