Updated `listRemoveAll` in the Redis, PostgreSQL, and MongoDB backends to accept either a single value or an array. Added a test for removing `['b', 'd']` and preserving the remaining order.

ESLint and `git diff --check` passed. The database list tests could not run because Redis at `127.0.0.1:6379` refused the connection.