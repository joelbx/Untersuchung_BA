# Checkpoint
Task: simplify SQLite access to a single *sql.DB connection.
Decision: follow the title and single-connection requirements; the final interface section contradicts them.
Changes: required SQLite DSN parameters, persistence transaction on supplied connection, transaction store in initial setup, focused tests.
Verification: go test ./db ./persistence ./server/... ./scanner passed; git diff --check passed.
