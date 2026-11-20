Implemented referential validation for flag rule variants and segments, including boolean rollouts. Validation errors now unwrap into individual errors formatted as `message (file line:column)`, and `flipt validate` uses the error-only API.

Added `StoreSnapshot`, `SnapshotFromFS`, and `SnapshotFromPaths`; snapshot construction now rejects unresolved references. Updated the valid CUE fixtures so their rule distributions match their declared variants.

Verified with `go test ./internal/cue ./internal/storage/fs ./cmd/flipt` and `git diff --check`; both passed.