# Checkpoint

Task: resolve inconsistent email confirmation pending, expiry TTL, expiration cleanup, and resend eligibility in `/app`.

Constraints: use checked-out repository code and tests only; do not request downloads or delegate; do not inspect credentials, private process files, benchmark solutions, or evaluator artifacts; preserve git history, index baseline, and harness configuration.

Findings: `src/user/email.js` sets the per-user marker to `emailConfirmInterval` minutes but hard-codes the confirmation record to one day. The database adapters provide `db.pttl`, and the resend path only checks for a pending marker. `emailConfirmExpiry` is not currently declared in defaults or exposed in the user settings page.

Plan: make both keys expire after `emailConfirmExpiry` days; add a pending-state check that strictly validates the backing confirmation record and optional email; add live TTL and resend eligibility APIs; use the new eligibility check when sending; and expose the expiry setting. Existing implementation tests are in `test/user.js` and `test/user/emails.js`.

Completed: `src/user/email.js` now validates the backing confirmation record and live marker TTL, exposes `getValidationExpiry` and `canSendValidation`, clears stale/expired validation data, applies configured expiry in milliseconds to both stored keys, and gates resend attempts with the configured interval. Added the one-day `emailConfirmExpiry` default and its admin setting/labels.

Validation: `test/user/emails.js` passed (6 tests) against a temporary local Redis instance; ESLint, `node --check`, JSON parsing, and `git diff --check` passed. The suite emitted a sendmail-not-found log, but all tests passed.

Final review complete: the working tree contains only the intended implementation, default, and settings UI/locale changes; no index or history changes were made.
