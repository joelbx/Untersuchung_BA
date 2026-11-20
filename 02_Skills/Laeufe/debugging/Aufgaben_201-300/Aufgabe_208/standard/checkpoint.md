# Email confirmation debugging checkpoint

Phase 1 started. Local repository at `/app`; `rg` is unavailable, so searches use `grep`/`find`. No source changes yet. Investigating pending marker, confirmation record, TTL, resend logic, and relevant tests before fixing.

Root cause: `src/user/email.js` sets `confirm:byUid` expiry to the resend interval (minutes) but sets `confirm:<code>` expiry to a fixed day. Pending state derives only from the marker, so it disappears while a usable confirmation record remains. The email-specific pending check can return `null`, violating boolean API. The send gate tests pending status alone, with no elapsed-interval calculation. `emailConfirmExpiry` has no configured default yet. Store adapters expose `db.pttl` in milliseconds; comparable confirmation patterns use `pexpireAt` and `expireValidation` deletes both keys.

Hypothesis: using one configured expiry deadline for both keys, then checking the marker's live TTL against the configured resend interval, will keep state and resend timing consistent. Test will cover strict booleans, TTL bounds, immediate/after-interval gating, and explicit expiry cleanup.

Reproduction: `./node_modules/.bin/mocha test/user.js --grep 'should track validation expiry' --timeout 25000` initially could not connect (`ECONNREFUSED 127.0.0.1:6379`); started the installed local Redis server without persistence and reran. It failed as expected at the strict false assertion (`null !== false`). After patch, the focused test passes. A broader `--grep 'email confirm'` run failed in a pre-existing profile test because that grep selected the assertion while excluding its prerequisite profile-update test. Full `test/user.js` run is needed to assess it in sequence.

Final patch: added `emailConfirmExpiry` default of one day; aligned marker and confirmation record expiries to one millisecond deadline; added strict boolean pending state, live millisecond TTL API, and resend eligibility API; wired sending through eligibility; retained explicit expiry cleanup. Regression test covers state, TTL bounds and reduction, resend timing, and cleanup.

Checks: `./node_modules/.bin/mocha test/user.js test/user/emails.js --timeout 25000` exited 0 (255 passing); focused regression rerun exited 0 (1 passing); `./node_modules/.bin/eslint src/user/email.js test/user.js`, `git diff --check`, and JSON parse of `install/data/defaults.json` exited 0. Full test run logged a sendmail-not-found error from a caught registration email path, but the suite passed. No remaining check is blocked.
