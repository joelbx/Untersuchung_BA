**Diagnosis:** `incrObjectFieldByBulk` is absent from both [Mongo hash.js](/app/src/database/mongo/hash.js:214) and [Redis hash.js](/app/src/database/redis/hash.js:198). The existing methods increment one field at a time.

Mongo can use one upserted `$inc` document per key to update that key’s fields atomically. Redis needs a per-key server-side operation that validates existing fields before applying `HINCRBY`; its current batch is a pipeline, which cannot roll back earlier field increments.

The main uncertainty is partial success across keys: an unordered Mongo bulk or Redis pipeline can succeed for some keys and fail for others. Cache eviction must follow the keys that actually changed. Existing [hash tests](/app/test/database/hash.js:617) do not cover the new API.

I recorded the findings in `.codex-role-output/checkpoint.md`. No source or tests were changed because this run’s specialist instructions limit work to fault localization.