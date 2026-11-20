Updated `listRemoveAll` in the Redis, MongoDB, and PostgreSQL adapters to accept multiple distinct strings in one call while preserving the order of remaining elements. Added a regression test that reads the list immediately after removal.

The Redis list suite passed (20 tests), as did ESLint and `git diff --check`. MongoDB and PostgreSQL runtime tests were not run in this local setup.