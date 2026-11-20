Implemented the single connection path. `persistence.New` retains its supplied `*sql.DB` for queries and transactions, and transaction callbacks now use their `tx` datastore. SQLite options are applied to default, in-memory, and configured database paths.

The final `dbxBuilder` and read/write split requirements conflict with the title and expected behavior, so I followed the single connection objective.

Validation passed: `go test ./db ./persistence ./core/scrobbler ./server ./server/nativeapi ./server/subsonic` and `git diff --check`.