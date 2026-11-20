# Checkpoint

Investigating object field selection across database backends.

Root cause: getObject/getObjects wrappers discard fields; Postgres getObjectFields/getObjectsFields aggregate an empty field list to null instead of returning stored data. Existing Mongo/Redis helpers already return complete data for []. Existing selected-field helper tests expect null-valued fields for missing keys, which conflicts with the new getObjects missing-key contract; adjust these tests to require falsy missing entries consistently.

Reproduction: `./node_modules/.bin/mocha test/database/hash.js --grep 'object field selection' --timeout 30000` initially failed because Redis at 127.0.0.1:6379 was not running (ECONNREFUSED). Started the installed local redis-server; the same regression then failed as expected because getObject returned an unrequested `first` field.

Fix: pass fields through Mongo, Redis, and Postgres wrappers; default helper fields to []; route Postgres empty selections to full reads; return null for missing selected objects. Postgres multi-read SQL distinguishes absent rows from present rows whose requested fields are absent.

Verification: `./node_modules/.bin/mocha test/database/hash.js --timeout 30000` passed (55 tests). `./node_modules/.bin/eslint src/database/mongo/hash.js src/database/postgres/hash.js src/database/redis/hash.js test/database/hash.js && git diff --check` passed. `command -v psql` and `command -v mongod` returned no executable, so live Postgres and MongoDB integration behavior remains unverified locally.
