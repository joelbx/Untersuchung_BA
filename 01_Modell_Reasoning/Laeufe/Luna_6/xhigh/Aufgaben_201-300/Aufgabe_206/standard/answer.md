Added a per-actor posting lock in [topics.js](/app/src/controllers/write/topics.js:14). Overlapping creates or replies from the same user or guest session now receive the route’s HTTP 400 `bad-request` response; the lock is released after the request completes.

ESLint passed, and all 229 tests in `test/topics.js` passed. `git diff --check` passed.