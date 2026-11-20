Implemented `incrObjectFieldByBulk` in both database adapters.

- Mongo uses per-key atomic `$inc` upserts.
- Redis uses an atomic per-key script that checks existing values before applying increments.
- Both validate the request, coalesce repeated keys, invalidate caches for successful keys, and return no data.

ESLint passes for both files. The existing hash tests could not run because Redis at `127.0.0.1:6379` was unavailable. The test run created an untracked Redis artifact; I removed it.