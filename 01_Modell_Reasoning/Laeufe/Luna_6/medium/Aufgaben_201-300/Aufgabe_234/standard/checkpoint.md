# Checkpoint

Task: simplify SQLite database access to one unified `*sql.DB`, following the issue title and expected behavior where contradictory read/write split requirements appear later.

Findings: checked-out code already uses `*sql.DB` from `db.Db()` for migration initialization and accepts that connection in `persistence.New()`. `WithTx()` already creates transactions through the same dbx connection and exposes the transaction-backed store to callbacks. No read/write connection abstraction exists in this checkout.

Changes: configured `db.Db()` connection paths with the required SQLite options: `cache=shared`, `_cache_size=1000000000`, `_busy_timeout=5000`, `_journal_mode=WAL`, `_synchronous=NORMAL`, `_foreign_keys=on`, and `_txlock=immediate`. The `:memory:` alias now retains a plain SQLite memory URI before these options are appended.

Verification: `go test ./db ./persistence` passed.
