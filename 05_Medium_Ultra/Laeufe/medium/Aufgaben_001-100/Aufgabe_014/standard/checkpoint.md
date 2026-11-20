# Checkpoint

Task: Fix the listed NodeBB notification, selector, quick search, hash, email, route, and template issues.

Status: Implemented in checked-out files. ESLint and `git diff --check` pass. Existing `test/database/hash.js` and `test/emailer.js` pass (71 tests) with a temporary local Redis instance, which has been stopped. The pre-existing untracked `appendonlydir/` was not changed.
