Task: Fix listRemoveAll so one call accepts an array of distinct strings.
Status: Implemented in Redis, MongoDB, and PostgreSQL backends. Added shared database regression test covering multiple values, duplicates in the list, absent requested value, order, and immediate read.
Verification: `./node_modules/.bin/mocha test/database/list.js` passed (20 tests) with a temporary local Redis server; `./node_modules/.bin/eslint src/database/redis/list.js src/database/mongo/list.js src/database/postgres/list.js test/database/list.js` passed; `git diff --check` passed. MongoDB and PostgreSQL were not available for integration runs.
Workspace: Existing untracked appendonlydir/ left untouched. Temporary Redis server stopped.
