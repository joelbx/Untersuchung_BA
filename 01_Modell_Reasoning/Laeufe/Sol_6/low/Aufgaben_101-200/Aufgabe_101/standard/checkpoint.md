Task: Fix list removal of multiple distinct strings in one call.
Status: Updated Redis, MongoDB, and PostgreSQL listRemoveAll to accept arrays. Added shared regression test. Redis test passed (3 passing) using a temporary local Redis server. ESLint and git diff --check passed. MongoDB and PostgreSQL integration tests were not run.
