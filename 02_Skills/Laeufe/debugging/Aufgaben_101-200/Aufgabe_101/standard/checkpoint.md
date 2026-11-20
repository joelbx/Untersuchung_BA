# Checkpoint

Task: Fix list removal of multiple distinct string values in one call.

Status: Investigating. `rg` is unavailable (`/bin/bash: rg: command not found`); using local `find` and `grep`. Pre-existing untracked `appendonlydir/` is untouched.

Root cause evidence: all three `listRemoveAll` implementations handle `value` as a scalar. Mongo converts an array to a comma-joined string; Redis passes the array to one `LREM`; Postgres casts it to `TEXT` for one `array_remove`. Existing append methods support arrays, but the removal test only covered a scalar. Hypothesis: normalizing array values and applying each removal (or one membership update) will preserve the order and make awaited reads consistent.

Regression test added to `test/database/list.js`. Initial check: `./node_modules/.bin/mocha test/database.js --grep 'should remove multiple distinct values while preserving order' --reporter dot` failed before tests with `connect ECONNREFUSED 127.0.0.1:6379` in the root before hook. A local Redis instance is available for rerun.

Confirmed regression: with a temporary local Redis server, the new test failed before the fix with `ReplyError: ERR wrong number of arguments for 'lrem' command`.

Fix: normalize scalar/array values in all three backends. Redis awaits one `LREM` per value; Mongo uses `$pull` with `$in`; Postgres filters the SQL array with ordinality to retain order.

Verification: `./node_modules/.bin/mocha test/database.js --grep 'List methods' --reporter dot` passed (20 passing); `./node_modules/.bin/eslint src/database/redis/list.js src/database/mongo/list.js src/database/postgres/list.js test/database/list.js` passed; `git diff --check` passed. Only Redis integration was runnable locally; Mongo and Postgres services are unavailable, so their query behavior was reviewed statically.
