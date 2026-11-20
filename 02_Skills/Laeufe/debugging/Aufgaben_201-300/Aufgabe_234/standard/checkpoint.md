# Checkpoint

## Task
Simplify SQLite access to one `*sql.DB` across db, persistence, and callers.

## Initial findings
- The issue text conflicts with its final requirement and interfaces section: those ask for the read/write split that the title and expected behavior request removing. I will use repository evidence to identify the current implementation and follow the stated simplification goal.
- `rg` is unavailable (`/bin/bash: line 1: rg: command not found`), so repository searches will use `find` and `grep`.

## Work log
- Phase 1: Checkout already has `Db() *sql.DB`, `New(*sql.DB)`, and one dbx builder for ordinary operations. `Db()` opens the configured path without the requested SQLite options. `WithTx()` uses its own dbx connection when present, but has a global `db.Db()` fallback. `core/scrobbler/play_tracker.go:incPlay` opens a transaction then makes all three updates through `p.ds`, so they bypass `tx`.
- Phase 2: Other transaction callbacks use repositories from `tx`; `incPlay` is the exception. dbx's `Transactional` is available on `*dbx.DB`.
- Phase 3 hypotheses: Appending the required DSN options at the open point configures each pooled SQLite connection. Replacing the three `p.ds` calls with `tx` puts all play count updates in the transaction. Retaining the original dbx connection in SQLStore removes the global fallback while keeping the same pool.
- Baseline `GOPROXY=off go test ./db ./persistence -run '^TestDB$|^TestPersistence$' -count=1` started; result pending.
- Baseline command exited 0 for `db` and `persistence`.
- Phase 4: Added and ran failing tests before changes: `GOPROXY=off go test ./db -run '^TestSQLiteDSN$' -count=1` failed to compile because `sqliteDSN` was absent; `GOPROXY=off go test ./core/scrobbler -run '^TestIncPlayUsesTransactionStore$' -count=1` failed with 3 operations outside the transaction; `GOPROXY=off go test ./server -run '^TestInitialSetupUsesTransactionStore$' -count=1` failed with 2 operations outside the transaction.
- Implemented one SQLite DSN constructor with all seven required settings, retained the passed dbx connection for `WithTx`, and routed operations in `incPlay` and `initialSetup` through the transaction store. The checkout had no `db.DB` interface or `dbxBuilder`; adding them would contradict the title and first four requirements, so they were not introduced.
- Verification: `GOPROXY=off go test ./db ./persistence ./core/scrobbler -count=1` passed after correcting a test assertion that assumed URL query order. `GOPROXY=off go test ./core/... ./server/... -count=1` passed before the final `initialSetup` fix. `GOPROXY=off go test ./db ./persistence ./core/scrobbler ./server -count=1` passed after it. `git diff --check` passed.
- Final rerun after the last test cleanup: `GOPROXY=off go test ./db ./persistence ./core/scrobbler ./server -count=1` exited 0; `git diff --check` exited 0.
