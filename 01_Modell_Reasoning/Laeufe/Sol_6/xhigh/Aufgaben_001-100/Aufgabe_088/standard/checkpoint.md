# Checkpoint

Task: Add optional field selection to `getObject` and `getObjects`, with empty arrays returning full stored objects across MongoDB, Postgres, and Redis.

Initial state: `appendonlydir/` is untracked; leave it untouched. Located hash implementations and existing hash tests. Next: inspect backend behavior, edit implementations, run relevant existing tests.

Implemented: Optional `fields = []` on object and field retrieval methods in all three backends. Empty arrays return full objects; selected fields include null for absent stored fields; `getObject`/`getObjects` return null for missing keys and preserve key order. Field helpers retain their established null-filled result for missing keys when fields are requested, since application callers rely on it.

Verified: Redis hash suite: 59 passing. Combined database, categories, groups, messaging, posts, topics, and user suites: 990 passing. ESLint and `git diff --check` pass. MongoDB/Postgres servers are unavailable locally; code was reviewed for their query behavior. A broader full-suite run stopped at an API schema assertion outside the focused suites. Temporary local Redis was used for tests and will be stopped. Existing untracked `appendonlydir/` left untouched.
