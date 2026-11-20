Vuls2 now checks database metadata and schema version before honoring `SkipUpdate`. A mismatch forces a download when updates are enabled and returns a clear error when they are skipped. Connection and metadata errors include the database path.

Regression tests passed, as did `GOTOOLCHAIN=local GOPROXY=off go test ./...` and `git diff --check`.