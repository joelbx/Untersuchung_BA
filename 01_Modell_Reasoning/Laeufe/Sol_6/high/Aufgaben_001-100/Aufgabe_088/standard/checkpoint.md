# Checkpoint

Task: support optional field selection and empty-field full-object semantics for object retrieval across MongoDB, PostgreSQL, and Redis.

Implemented in `src/database/{mongo,postgres,redis}/hash.js`. Object wrappers accept optional `fields`, preserve missing keys as `null`, and field helpers return full objects for omitted or empty fields. Existing helper behavior for missing keys with selected fields remains an object with requested fields set to `null`.

Updated `test/database/hash.js` for selection, missing fields and keys, key order, duplicate keys, empty and omitted fields, and dotted field names.

Verification: Redis hash suite 60 passing; ESLint on changed JavaScript files and `git diff --check` passed. MongoDB and PostgreSQL services were not available for integration tests. Existing untracked `appendonlydir/` was present at start and left untouched.
