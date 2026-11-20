# Checkpoint

Issue: simplify SQLite access to one unified `*sql.DB` connection.

Implemented:
- Kept `db.Db()` and `persistence.New(*sql.DB)` as the single connection path, with migrations running through `db.Db()`.
- Applied the required SQLite URI options to the configured database path and updated the default path.
- Removed the persistence transaction fallback to the global singleton. Transactions use the store builder, and nested `WithTx` calls reuse the active transaction.

Validation:
- `go test ./db ./persistence` passed.
- `git diff --check` passed.

The later split-interface/dbxBuilder wording conflicts with the issue’s title and primary expected behavior, so no read/write split was introduced.
