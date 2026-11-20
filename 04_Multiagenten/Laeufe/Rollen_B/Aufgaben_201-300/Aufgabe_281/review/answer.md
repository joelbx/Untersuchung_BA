VERDICT: FIX

**Code defect:** Mongo accepts a field named `bad.field` even though the requirements say to reject it. [increment.js](/app/src/database/increment.js:18) checks for dots after [hash.js](/app/src/database/mongo/hash.js:267) passes the name through `fieldToString`, which replaces the dot. A direct local call returned an update for `bad.field` instead of throwing. Validate the original field name before normalization.

**Tests:** `timeout 55s ./node_modules/.bin/mocha test/database.js --grep 'incrObjectFieldByBulk'` passed with 4 tests after I started a temporary Redis server. `timeout 55s ./node_modules/.bin/mocha test/database.js --grep 'Hash methods'` passed with 68 tests. I stopped the server afterward.

**TEST_ENVIRONMENT_PROBLEM:** The first targeted run failed in setup with `ECONNREFUSED 127.0.0.1:6379`. Mongo tests could not run because `mongod` is unavailable locally. The Redis results do not cover the Mongo defect.