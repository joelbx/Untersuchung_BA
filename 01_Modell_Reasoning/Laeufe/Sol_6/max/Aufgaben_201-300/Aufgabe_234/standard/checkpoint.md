# Checkpoint

- Task: resolve SQLite database access issue in `/app`.
- Finding: `db.Db()` and `persistence.New()` already use `*sql.DB`; no `db.DB` split exists in this checkout. The read/write interface bullets conflict with the issue's stated goal, so the single-connection design is retained.
- Edited SQLite DSN to set all requested parameters, made `SQLStore.WithTx` use its supplied connection, and switched transaction callback operations in scrobbling and initial setup to `tx`.
- Existing tests passed: `go test ./db ./persistence ./core/scrobbler ./server -count=1` with `GOPROXY=off`.
- Added focused tests for the DSN and its effective SQLite PRAGMAs, plus transaction use of an isolated supplied `*sql.DB`.
- Final checks passed: `GOPROXY=off go test ./db ./persistence ./core/scrobbler ./server -count=1`; `GOPROXY=off go test ./scanner ./cmd ./core -count=1`; `git diff --check`.
- Work complete. Read/write routing interfaces and `dbxBuilder` were not added because they contradict the requested single-connection simplification.
