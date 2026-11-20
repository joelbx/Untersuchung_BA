# Checkpoint

Investigating reserved system tags. `rg` is unavailable (`/bin/bash: rg: command not found`); using local grep/find. No code changes yet.

## Root cause and hypothesis
`Topics.validateTags(tags, cid)` only checks category min/max counts; create and edit call it without a uid, and queue validation omits cid. `SocketTopics.isTagAllowed` only checks the category whitelist. No `systemTags` default exists. Thus neither server write paths nor the composer preflight can distinguish reserved tags from ordinary tags. Existing `User.isPrivileged(uid)` covers administrators, global moderators, and category moderators. Hypothesis: adding uid-aware validation of configured reserved tags at the shared validator, and the same privilege check in the socket preflight, will reject unprivileged assignment while preserving privileged use. Test this before the fix.

## Test environment
Initial pre-fix command: `./node_modules/.bin/mocha test/topics.js --grep 'reserved system tags'` exited 1 before any test: `Redis connection to 127.0.0.1:6379 failed - connect ECONNREFUSED 127.0.0.1:6379`. Local `redis-server` is available; starting a disposable local instance to run the existing tests.

## Additional API boundary
A review found `src/controllers/write/topics.js` calls `createTags` directly for `PUT /api/v3/topics/:tid/tags`, bypassing `validateTags`. Added a focused test; before the route fix, `./node_modules/.bin/mocha test/topics.js --grep 'reserved system tags'` exited 1 with `AssertionError: Missing expected rejection` in the tagging API test. The route now validates the complete resulting tag list and caller uid before writing.

## Verification
- Pre-fix reserved-tag test: failed at expected missing rejection.
- Post-fix `./node_modules/.bin/mocha test/topics.js test/categories.js`: exit 0, 223 passing.
- `./node_modules/.bin/mocha test/posts.js`: exit 0, 99 passing (existing upload fixture warnings appeared).
- `./node_modules/.bin/eslint src/topics/tags.js src/topics/create.js src/posts/edit.js src/posts/queue.js src/socket.io/topics/tags.js src/controllers/write/topics.js test/topics.js`: exit 0.
- `git diff --check`: exit 0.
