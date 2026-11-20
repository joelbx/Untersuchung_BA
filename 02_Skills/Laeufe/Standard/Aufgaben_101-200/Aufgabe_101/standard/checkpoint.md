# Checkpoint

Task: fix `listRemoveAll` for an array of distinct strings.

Implemented in Redis, MongoDB, and PostgreSQL adapters. Redis removes each requested value before resolving. MongoDB uses one `$pull` with `$in`. PostgreSQL filters its array with `UNNEST ... WITH ORDINALITY` so remaining order is preserved. Existing falsy-key handling remains in each adapter. Added a shared database regression test that removes `b` and `d` from `['a', 'b', 'c', 'd', 'e', 'b']` and immediately reads `['a', 'c', 'e']`.

Checks:
- `./node_modules/.bin/eslint src/database/redis/list.js src/database/mongo/list.js src/database/postgres/list.js test/database/list.js` — passed.
- `./node_modules/.bin/mocha test/database.js --grep 'List methods'` — first attempt failed in setup: `Error: connect ECONNREFUSED 127.0.0.1:6379` (local Redis was not running). Started the installed local Redis server without persistence and reran the exact command: 20 passing. Stopped that server after the run.
- `git diff --check` — passed.
- MongoDB and PostgreSQL integration tests were not run; local test configuration selected Redis and no other local backend was set up. Their adapter changes were linted, but their runtime behavior remains unverified here.

`rg` was unavailable (`/bin/bash: rg: command not found`), so repository searches used `find` and `grep`.
