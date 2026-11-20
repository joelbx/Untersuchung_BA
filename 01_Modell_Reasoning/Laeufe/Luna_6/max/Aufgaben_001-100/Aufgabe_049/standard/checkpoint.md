# Checkpoint

Task: Resolve the ACP email validation issue in `/app`.

Implemented:
- Confirmation records now use `confirm:byUid:<uid>` mappings and `confirm:<code>` objects with an explicit millisecond `expires` timestamp.
- Added `getEmailForValidation`, expiry-aware `isValidationPending`, and `expireValidation`; confirmation and ACP validation use the profile email first and fall back to mapped confirmation data.
- Non-forced sends stop when a confirmation is still active; forced sends replace it. Explicit attempts to submit the current email as a change are rejected. Profile email changes force a replacement confirmation.
- Admin user rows show Validated, Validation Pending, Validation Expired, or (no email), including confirmation-email fallback. User deletion removes the confirmation mapping, mapped object, and send marker.
- Confirmation sends are serialized per UID within the app process to prevent simultaneous requests creating mismatched codes.

Verification:
- ESLint, JavaScript syntax checks, language JSON parsing, and `git diff --check` passed.
- `npm test -- test/user.js`: 133 passing, 1 failing. The remaining test expects `socketUser.emailConfirm` to resend while a non-expired confirmation is pending; the new requirement disallows a resend unless `force` is provided.
- Local Redis used for the suite has been stopped.
