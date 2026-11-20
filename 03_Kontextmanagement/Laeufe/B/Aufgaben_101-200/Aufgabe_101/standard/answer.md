Updated `listRemoveAll` in the Redis, MongoDB, and PostgreSQL backends to remove multiple string values in one call while preserving the order of the remaining list. Added a shared test that reads the list immediately after removal.

The Redis list suite passed (20 tests), as did lint and diff checks. MongoDB and PostgreSQL integration tests were not run.