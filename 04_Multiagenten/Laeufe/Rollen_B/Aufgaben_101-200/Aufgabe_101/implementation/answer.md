Updated `listRemoveAll` in Redis, MongoDB, and PostgreSQL to remove every requested string while preserving the order of the remaining list. Added a regression test that reads the list immediately after removal.

Lint, syntax checks, and `git diff --check` pass. The targeted database test could not run because Redis at `127.0.0.1:6379` refused the connection.