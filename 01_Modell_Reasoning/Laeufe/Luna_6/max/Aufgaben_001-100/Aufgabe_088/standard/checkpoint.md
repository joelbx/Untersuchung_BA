# Checkpoint

Task: fix `db.getObject`/`getObjects` field selection consistently across MongoDB, Postgres, and Redis, including empty-field full-object behavior, nulls for missing requested fields, missing-key values, and input order.

Constraints: use local repository code/tests only; do not read credentials, private process files, benchmark solutions, or evaluator artifacts. Do not alter git history, index baseline, or harness configuration.

Progress: checkpoint created before implementation. Initial status shows an unrelated untracked `appendonlydir/`; leave it untouched.

Implementation complete:
- Added optional `fields` support to `getObject`/`getObjects` for MongoDB, Postgres, and Redis.
- Made omitted or empty field lists return full stored objects in both wrappers and field helpers, including Postgres JSONB selection.
- Kept missing requested fields as `null`; public `getObject(s)` preserve falsy results for absent keys and array order.
- Replaced conditional `getObjectsFields`/`getObjects` selection in messaging, posts, topics, categories, and groups with `getObjects(keys, fields)`.

Validation:
- Existing `test/database/hash.js` selected object retrieval suites: 9 passing, run against a temporary in-memory Redis adapter to avoid loading credentials or external services.
- Credential-free mock-client smoke checks for MongoDB, Postgres, and Redis passed for fields, empty lists, missing requested fields, missing keys, and order.
- ESLint, Node syntax checks, and `git diff --check` passed.
