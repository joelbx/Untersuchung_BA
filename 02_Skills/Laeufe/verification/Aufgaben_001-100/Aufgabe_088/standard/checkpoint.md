# Checkpoint

Task: add optional field selection to db.getObject and db.getObjects, with empty arrays returning complete objects across MongoDB, Postgres, and Redis.

Status: inspecting implementations and tests. Verification pending.

Verification so far:
- `./node_modules/.bin/mocha test/database/hash.js --reporter dot` failed before tests: `connect ECONNREFUSED 127.0.0.1:6379` (0 passing, 1 failing). Redis service was unavailable; integration behavior remains unverified.
- `./node_modules/.bin/eslint src/database/mongo/hash.js src/database/redis/hash.js src/database/postgres/hash.js test/database/hash.js` exited 0.
- `git diff --check` exited 0.

Final verification:
- Started a temporary local Redis instance with `redis-server --bind 127.0.0.1 --port 6379 --save '' --appendonly no --daemonize yes --pidfile /tmp/codex-issue-redis.pid`.
- `./node_modules/.bin/mocha test/database/hash.js --reporter dot` exited 0: 57 passing.
- `./node_modules/.bin/eslint src/database/mongo/hash.js src/database/redis/hash.js src/database/postgres/hash.js test/database/hash.js` exited 0.
- `node --check` on all four touched JavaScript files exited 0.
- `git diff --check` exited 0.
- MongoDB and Postgres integration tests were not run because those local database servers are unavailable; their runtime behavior remains unverified.
