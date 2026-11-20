Task: Repair ACP email validation and confirmation lifecycle.
Implemented: per-user confirmation code index, explicit millisecond expiry, pending/expiry helpers, primary/pending email lookup, stale-code invalidation, confirmation cleanup on validation and account deletion, ACP four-state email status, forced profile replacement, and focused lifecycle tests.
Checks:
- `node_modules/.bin/eslint src/user/email.js src/user/delete.js src/user/create.js src/user/profile.js src/controllers/admin/users.js public/src/admin/manage/users.js test/user.js` passed.
- `node_modules/.bin/mocha test/user.js --grep '^User email confirm' --exit` passed (5).
- `node_modules/.bin/mocha test/user.js --grep '^User profile methods' --exit` passed (42).
- `git diff --check` passed.
- Full `node_modules/.bin/mocha test/user.js --exit` reached 173 passing, then failed in an unrelated invite group membership test: `User invites after invites checks should joined the groups from invitation after registration: Error: Not joined to the groups` (test/user.js:2363). The run preceded the account creation adjustment; focused tests after that adjustment passed.
- Initial test command could not connect to Redis (`ECONNREFUSED 127.0.0.1:6379`); local redis-server was started and tests were rerun.
- `node_modules/.bin/mocha test/user.js --grep '^User invites' --exit` also failed at the same invitation membership assertion (25 passing, 1 failing), confirming the failure reproduces when run separately. Its cause was not established; confirmation/profile tests pass.
