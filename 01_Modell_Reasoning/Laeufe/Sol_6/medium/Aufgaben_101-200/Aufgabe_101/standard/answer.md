Updated `listRemoveAll` in the Redis, MongoDB, and PostgreSQL backends to remove every requested string while preserving the order of the remaining list. Added a regression test that reads the list immediately after removal.

The Redis list suite passes (20 tests), and lint passes. MongoDB and PostgreSQL integration tests could not run because those services were unavailable.