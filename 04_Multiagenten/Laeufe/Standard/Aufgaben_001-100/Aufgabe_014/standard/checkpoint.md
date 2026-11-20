# Checkpoint

Issue: NodeBB v4.4.3 notification dropdown and related fixes.
Status: Implemented all requested repository changes in checked-out files.
Validation: ESLint on edited JavaScript passed; `git diff --check` passed; selected existing Mocha suites (`test/database/hash.js`, `test/emailer.js`, `test/notifications.js`) passed, 102 tests. Local Redis was started for the tests and stopped afterward.
Note: `appendonlydir/` was already untracked and was left untouched.
