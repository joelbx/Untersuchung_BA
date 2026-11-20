# Checkpoint

Resolved SQLite access around one `*sql.DB` pool. The checkout already used `*sql.DB` for `db.Db()` and `persistence.New()`; the issue's final bullet and INTERFACES section conflict with its title, expected behavior, and first four requirements. Followed the single-connection intent and did not add a read/write interface or builder.

Changes:
- `db.Db()` applies `cache=shared`, `_cache_size=1000000000`, `_busy_timeout=5000`, `_journal_mode=WAL`, `_synchronous=NORMAL`, `_foreign_keys=on`, and `_txlock=immediate` to every configured SQLite path. Existing unrelated query parameters are preserved.
- `persistence.WithTx()` uses its supplied connection and passes the transaction builder to repositories. Nested `WithTx()` calls reuse the current transaction.
- Added focused tests for DSN parameters and commit/rollback on a caller supplied connection.

Checks passed:
- `GOPROXY=off GOSUMDB=off go test ./db ./persistence ./scanner ./cmd`
- `git diff --check`

`rg` is unavailable (`/bin/bash: rg: command not found`); used `find` and `grep`.
