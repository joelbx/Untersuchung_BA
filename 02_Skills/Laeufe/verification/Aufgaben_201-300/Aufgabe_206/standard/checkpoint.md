# Checkpoint

Task: prevent overlapping topic creation by the same actor from creating duplicate topics.

Implementation: added `lockPosting(req, error)` in `src/controllers/write/topics.js`, keyed by authenticated uid or guest session ID. Create and reply hold the lock through posting and response formatting, then release it in `finally`.

Regression test: `test/topics.js` sends a minimal valid topic payload in overlapping authenticated requests while the first post is held. It checks HTTP 200/`ok` for one request, HTTP 400/`bad-request` for three others, one call to the post operation, and increments of exactly one in global topic/post, category topic, and user topic counts.

Verification:
- Initial `./node_modules/.bin/mocha test/topics.js --grep 'rejects overlapping API topic creates'` failed before tests: `connect ECONNREFUSED 127.0.0.1:6379`. A locally installed Redis server was started without downloads; the test was then run.
- Red check with the create guard temporarily removed: `./node_modules/.bin/mocha test/topics.js --grep 'rejects overlapping API topic creates'` exited 1 with `AssertionError: 200 !== 400`.
- Green check with the guard restored: `./node_modules/.bin/mocha test/topics.js` exited 0, 230 passing.
- `./node_modules/.bin/eslint src/controllers/write/topics.js test/topics.js` and `git diff --check` exited 0 before the red/green check; final runs follow.

Automatic approval review rejected a temporary backup command because it contained `rm -f`; a direct reversible source edit was used for the red/green check instead.
