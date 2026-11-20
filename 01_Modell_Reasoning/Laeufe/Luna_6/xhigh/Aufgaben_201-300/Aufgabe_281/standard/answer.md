Implemented bulk increments with input validation, safe integer checks, field sanitization, upsert behavior, per-object atomicity, and cache invalidation for successful keys. Mongo uses unordered `$inc` upserts; Redis uses a pipeline of atomic scripts that validate each hash before applying `HINCRBY`.

Lint, syntax checks, input validation checks, Redis integration checks, and Mongo mock-backed checks passed. The existing database hash suite was not run because its harness reads and logs `config.json`, which may contain credentials.

Changes are in [database helpers](/app/src/database/helpers.js:30), [Mongo hash](/app/src/database/mongo/hash.js:265), and [Redis hash](/app/src/database/redis/hash.js:340).