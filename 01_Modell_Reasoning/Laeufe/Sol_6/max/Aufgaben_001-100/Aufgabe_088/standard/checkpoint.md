# Checkpoint

Task: support optional field selection for `getObject` and `getObjects` across MongoDB, Postgres, and Redis, while treating an empty field list as a full-object request.

Status: complete. `getObject` and `getObjects` accept optional field lists across Redis, MongoDB, and Postgres. Empty field lists return complete objects for all four read methods. Selected reads return null for missing objects; legacy field helpers retain null-filled maps for missing objects when fields are requested.

Verification: 784 passing in the database, posts, topics, categories, groups, and messaging suites; 59 passing in the final focused hash suite. ESLint and `git diff --check` pass. Integration tests used the configured Redis backend; MongoDB and Postgres were reviewed statically because local services are unavailable.

The pre-existing untracked `appendonlydir/` is outside this task.
