# Checkpoint

Issue: implement `incrObjectFieldByBulk` for Mongo and Redis hash backends.

Implemented validated per-key bulk increments in Mongo (`$inc` with conditional update) and Redis (Lua validation plus `HINCRBY`), with cache invalidation after successful key updates. Empty input returns before backend/cache access.

Next: run existing hash/database tests and lint the edited files; inspect the final diff.
