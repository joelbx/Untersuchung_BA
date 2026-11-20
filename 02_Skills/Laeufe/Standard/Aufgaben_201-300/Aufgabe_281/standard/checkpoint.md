# Checkpoint

Task: implement `incrObjectFieldByBulk` for Mongo and Redis hash backends, validate input, preserve per-key atomicity, and invalidate caches after writes.

Initial state: `rg` is unavailable (`/bin/bash: rg: command not found`); using local `grep`/`find`. Existing untracked `appendonlydir/` left untouched.

Status: implemented and verified.

Changes:
- Shared tuple and safe-integer validation in `src/database/hashBulkIncrements.js`.
- Mongo unordered `bulkWrite` with one `$inc` upsert per key; evicts successful keys, including partial successes. Duplicate-key upsert races are retried for the affected keys.
- Redis pipelined Lua calls that validate every field before applying that key's `HINCRBY` operations; evicts successful keys.
- Integration cases added to `test/database/hash.js`.

Checks:
- `./node_modules/.bin/mocha test/database/hash.js --grep 'incrObjectFieldByBulk'`: passed after starting a temporary local Redis service.
- `./node_modules/.bin/mocha test/database/hash.js`: passed with the same temporary Redis service.
- `./node_modules/.bin/eslint src/database/hashBulkIncrements.js src/database/mongo/hash.js src/database/redis/hash.js test/database/hash.js`: passed.
- `git diff --check` and `node --check` on the three implementation files: passed.
- A local stub assertion checked Mongo `bulkWrite` shape, duplicate tuple coalescing, rejected invalid increments, and empty-array behavior: passed.
- Initial focused Mocha run without Redis: failed with `Error: connect ECONNREFUSED 127.0.0.1:6379`; rerun passed after starting local Redis. Redis was stopped after checks.

Mongo integration was not run because `mongod` is unavailable locally. Mongo behavior follows its existing `$inc` and cache patterns; the unordered bulk partial-error path is not integration verified.
