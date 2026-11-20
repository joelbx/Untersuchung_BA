Updated `listRemoveAll` in the Redis, MongoDB, and PostgreSQL adapters to remove multiple distinct string values in one call while preserving the order of the remaining items. Added a shared regression test that reads the list immediately after removal.

The Redis regression suite passed (3 tests), as did ESLint and `git diff --check`. MongoDB and PostgreSQL integration tests were not run.