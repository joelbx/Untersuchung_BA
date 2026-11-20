# Checkpoint

Task: Fix email confirmation pending state, live TTL, expiration cleanup, and resend eligibility.

Implemented: Strict pending boolean with stored-email check; live millisecond TTL; configured expiry for marker and record; resend interval gating; one-day default for emailConfirmExpiry. Added six regression tests in test/user-email-validation.js.

Verification: `./node_modules/.bin/mocha test/user-email-validation.js --reporter dot` passed (6 tests). `./node_modules/.bin/eslint src/user/email.js test/user-email-validation.js` passed. Initial `npm test` failed before tests with `Error: connect ECONNREFUSED 127.0.0.1:6379` in the before-all hook for `should grab all mounted routes and ensure a schema exists`. Started the installed local Redis server; full `npm test` rerun is in progress.

Full `npm test` with local Redis: 1028 passing, then failed at `Admin Controllers > should load /admin/extend/plugins` because `assert(body.hasOwnProperty('installed'))` was false (`test/controllers-admin.js:249`). A filtered `mocha test/user.js test/user/emails.js --grep 'email confirm|send validation email|email confirmation'` run had 1 passing then failed at `User > profile methods > .updateProfile() > should also generate an email confirmation code for the changed email` (`test/user.js:896`) because the grep omitted its prerequisite profile update test. Running both test files without grep now.

Final verification: `./node_modules/.bin/mocha test/user.js test/user/emails.js --reporter dot` passed (254 tests). `./node_modules/.bin/mocha test/user-email-validation.js --reporter dot` passed (6 tests). `./node_modules/.bin/eslint src/user/email.js test/user-email-validation.js` and `git diff --check` passed. The full `npm test` did not pass because of the admin plugins assertion noted above; email tests pass independently. The focused grep failure was a test-selection artifact and is resolved by running the full user/email test files.
