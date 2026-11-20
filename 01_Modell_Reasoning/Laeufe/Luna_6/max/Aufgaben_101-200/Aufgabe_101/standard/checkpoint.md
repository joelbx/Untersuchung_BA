# Checkpoint

Task: fix list removal so an array of distinct string elements is removed from a target list in one call, preserving remaining order and immediate read consistency.

Implemented array removal in the MongoDB, PostgreSQL, and Redis adapters. The MongoDB update removes all matching array members; PostgreSQL filters by the requested values while preserving ordinality; Redis removes each value in one transaction. Added a database regression test for `['a', 'b', 'c', 'd', 'e']` minus `['b', 'd']`.

`node --check` passed for all changed JavaScript files, ESLint passed for the changed files, and `git diff --check` passed. The integration test depends on `test/mocks/databasemock.js`, which loads `/app/config.json`; I have not run it because that would read local database credentials, which this task forbids. Existing untracked `appendonlydir/` is pre-existing and remains untouched.
