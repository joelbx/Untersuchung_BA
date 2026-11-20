# Checkpoint

Issue: add optional field selection to `db.getObject` and `db.getObjects`, with empty fields meaning the full stored object consistently across MongoDB, Postgres, and Redis.

Implemented optional `fields = []` arguments for `getObject`/`getObjects` in all three backends. Empty or invalid field lists use full-object retrieval, and explicit field selections retain null values for absent fields and input key ordering. Postgres helper behavior now matches the same empty-list and missing-key contracts.

Validation: ESLint passed for the three modified backend files; `git diff --check` passed. The existing hash test suite was attempted, but its global setup could not connect to Redis at `127.0.0.1:6379` (`ECONNREFUSED`). The attempt-generated Redis files were removed.
