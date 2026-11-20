# Checkpoint

Task: Support optional field selection on object retrieval across MongoDB, Postgres, and Redis.

Completed: Updated all three backends. Empty field lists return complete objects for both wrapper and helper methods. Selected fields include null for absent fields, and getObjects preserves key order with null entries for missing keys. Added regression cases to the existing hash suite.

Verification: `./node_modules/.bin/mocha test/database/hash.js --reporter dot` passed (57 tests) using a temporary local Redis server. ESLint on touched files and `git diff --check` passed. MongoDB and Postgres integration tests were unavailable locally.
