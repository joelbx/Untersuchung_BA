# Checkpoint

Task: simplify SQLite access to one `*sql.DB` connection.

Decision: the issue text conflicts with itself. Its title, problem, expected behavior, and first four requirements call for a unified connection; the final requirement and INTERFACES section call for restoring read/write separation. Implemented the unified connection direction. The checked-out repository already had `Db() *sql.DB` and `New(*sql.DB)`, with no `db.DB` interface or `dbxBuilder`.

Changes:
- `db.Db()` adds the requested SQLite DSN parameters to the one connection pool, preserving other query parameters.
- `SQLStore` retains its supplied dbx connection for transactions and uses the transaction builder for repositories. Removed global fallback and redundant builder accessor.
- Added DSN and supplied-connection transaction tests.

Verification:
- `GOPROXY=off GOSUMDB=off go test -count=1 ./db ./persistence ./cmd ./scanner` exited 0; db, persistence, scanner passed; cmd has no tests.
- `git diff --check` exited 0.
- `GOPROXY=off GOSUMDB=off go test ./...` exited 1. Two tests in `scanner/metadata/taglib` fail at `taglib_test.go:98`: AAC gain-tag cases receive duplicate `replaygain_album_gain` values `["0.37", "0.37"]` instead of one `["0.37"]`. The affected database packages passed in that run. No taglib files were changed; full-suite status remains failing.
- `rg` unavailable (`/bin/bash: rg: command not found`); used `find`/`grep` for repository inspection.
