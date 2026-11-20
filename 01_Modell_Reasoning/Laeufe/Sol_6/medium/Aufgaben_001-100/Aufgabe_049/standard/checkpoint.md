Task: Fix ACP email validation actions and statuses, confirmation storage, and account deletion cleanup.
State: Complete. Two-key confirmation records use explicit expiry. ACP uses profile/pending email lookup, displays four statuses, and refreshes after actions. Confirmation and deletion remove both keys. Creation waits for initial confirmation storage to avoid a resend race.
Verification: ESLint passed on touched JavaScript; focused Mocha user and socket validation suites passed (8 tests); git diff --check passed. Temporary local Redis test server was stopped.
Constraints observed: Local repository and existing tests only; git history, index baseline, and harness configuration untouched.
