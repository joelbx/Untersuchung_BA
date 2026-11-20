# Checkpoint

Resolved the unified SQLite connection request in checked-out files.
- `db.Db()` remains the single `*sql.DB` provider and now applies all required SQLite DSN options.
- Persistence transactions use the connection supplied to `New()`; the global connection fallback was removed.
- Scrobble play-count updates use the transaction store inside `WithTx`.
- Added focused tests for DSN options and an isolated persistence connection.
- Verified: `GOPROXY=off GOSUMDB=off go test ./db ./persistence ./core/scrobbler` passed.

The issue text's final bullet and INTERFACES section ask for read/write separation, which conflicts with its title, problem statement, and first four requirements. The implementation follows the unified-connection behavior.
