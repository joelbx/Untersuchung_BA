VERDICT: FIX

**Code review:** I found no correctness defect in the patch’s field selection, missing field, missing key, or input order handling across MongoDB, Postgres, and Redis.

**TEST_ENVIRONMENT_PROBLEM:** `./node_modules/.bin/mocha test/database/hash.js` exited 1 before the hash tests ran: `connect ECONNREFUSED 127.0.0.1:6379` (0 passing, 1 failing). Make the configured isolated Redis test service available and rerun that command. The relevant tests have not passed, so I cannot accept the patch.

The local ESLint command covering all nine changed JavaScript files exited 0. I recorded the review in [checkpoint.md](/app/.codex-role-output/checkpoint.md).