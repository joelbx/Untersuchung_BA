# Checkpoint

Issue: add optional field selection to `db.getObject` and `db.getObjects` across MongoDB, Postgres, and Redis. Empty field lists must fetch full objects; selected missing fields must be null; preserve key order and missing-key behavior.

Implemented optional `fields = []` on object retrieval methods in Redis, MongoDB, and Postgres. Public methods return only requested fields, null for absent fields, and null for missing objects. Empty lists and omitted lists return full objects, including through the field helpers. Postgres selected reads use a projection query while preserving input order. Existing selected-helper missing-key behavior remains intact.

Added regression cases to `test/database/hash.js`. Redis hash suite: 59 passing. ESLint and `git diff --check`: passing. MongoDB and Postgres integration services were unavailable. No delegation used. An unrelated untracked `appendonlydir/` was present initially and left untouched.
