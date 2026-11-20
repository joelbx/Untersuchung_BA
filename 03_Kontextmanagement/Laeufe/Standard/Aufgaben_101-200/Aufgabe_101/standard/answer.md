Updated `listRemoveAll` in the MongoDB, Redis, and PostgreSQL backends to remove every requested string while preserving the order of the remaining list. Added a shared regression test that reads the list immediately after removal.

ESLint and `git diff --check` passed. The existing list methods suite passed against Redis (20 tests). MongoDB and PostgreSQL integration tests were not run.