# Checkpoint

Implemented `incrObjectFieldByBulk` in Mongo and Redis hash adapters.

- Validates tuple shape, field names, and safe integer increments before backend calls; duplicate keys are combined.
- Mongo uses per-key atomic `$inc` upserts. Redis uses a per-key Lua operation that checks existing hash fields before applying any `HINCRBY`, preserving per-key atomicity.
- Successful keys have their cache entries invalidated; empty input returns before database/cache calls.

Verification: ESLint passes for both changed adapter files. `npx mocha test/database/hash.js` could not run because the configured Redis service at `127.0.0.1:6379` is unavailable (ECONNREFUSED).
