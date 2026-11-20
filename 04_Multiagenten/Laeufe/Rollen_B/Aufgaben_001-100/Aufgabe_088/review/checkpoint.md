VERDICT: FIX

Reviewed the MongoDB, Postgres, and Redis hash implementations, changed callers, and existing hash tests. No code defect found in the requested field selection, missing field, missing key, or ordering behavior.

TEST_ENVIRONMENT_PROBLEM: `./node_modules/.bin/mocha test/database/hash.js` exited 1 before tests ran: `connect ECONNREFUSED 127.0.0.1:6379`; 0 passing, 1 failing. The configured isolated Redis test service must be available, then rerun this suite. Because a relevant test could not execute successfully, verdict is FIX.

`./node_modules/.bin/eslint src/database/mongo/hash.js src/database/postgres/hash.js src/database/redis/hash.js src/categories/data.js src/groups/data.js src/messaging/data.js src/posts/data.js src/topics/data.js test/database/hash.js` exited 0.
