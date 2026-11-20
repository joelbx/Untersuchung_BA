Task: Optional field selection for getObject/getObjects, with empty fields returning full objects across MongoDB, Postgres, Redis.
Status: Implemented in all three backend hash modules. Added coverage in test/database/hash.js for selected fields, missing fields/keys, order, and empty/omitted fields. Redis and MongoDB preserve legacy getObjectsFields missing-key objects for helper callers; wrappers return null for missing keys. Postgres now does the same.
Checks:
- ./node_modules/.bin/eslint src/database/mongo/hash.js src/database/postgres/hash.js src/database/redis/hash.js test/database/hash.js — passed.
- ./node_modules/.bin/mocha test/database/hash.js --timeout 25000 — 57 passing against local Redis.
- git diff --check — passed.
Initial test attempt: ./node_modules/.bin/mocha test/database/hash.js --grep 'getObject| getObjects' --timeout 10000 failed with `Error: connect ECONNREFUSED 127.0.0.1:6379`; started installed local redis-server and reran successfully. MongoDB/Postgres integration tests remain unverified because those servers are unavailable locally.
