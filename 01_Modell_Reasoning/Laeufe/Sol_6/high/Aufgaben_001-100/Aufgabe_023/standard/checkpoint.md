# Checkpoint

Task: make authentication database initialization and cleanup depend on enabled methods that require persistent storage.

Implemented: method metadata declares database dependency; config checks enabled methods for database use and cleanup; auth startup uses memory storage and still builds JWT middleware when no database is needed; cleanup skips disabled and non-database methods. Added configuration, startup, and cleanup regression coverage.

Verification complete: `GOPROXY=off GOSUMDB=off go test ./internal/config ./internal/cmd ./internal/cleanup` passes. `git diff --check` passes. Restored the unrelated `go.work.sum` changes caused by the Go tool.
