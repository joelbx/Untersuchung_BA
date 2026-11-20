# Vuls2 schema mismatch fix

Implemented in `detector/vuls2/db.go`: `shouldDownload` reads metadata before honoring SkipUpdate, forces download on schema mismatch, and reports mismatches when updates are disabled. `newDBConnection` opens and validates metadata and schema version, includes the database path in connection and metadata errors, then closes the connection for the caller to open.

Added local tests in `detector/vuls2/db_test.go` for mismatch decisions, mismatch error path, missing metadata, and connection reuse.

Checks passed: `gofmt -w detector/vuls2/db.go detector/vuls2/db_test.go`; `git diff --check`; `GOPROXY=off GOSUMDB=off go test ./detector/vuls2` (`ok ... 0.389s`). `rg` was unavailable (`/bin/bash: rg: command not found`); local inspection used `grep` and `find`.
