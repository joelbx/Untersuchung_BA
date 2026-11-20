# Checkpoint

Implemented location-aware, multi-error validation with rule variant and segment reference checks. `SnapshotFromFS` and `SnapshotFromPaths` check references before assembling snapshots, and imports run the same reference checks before writing resources so invalid imports fail consistently without partial writes. Exported `StoreSnapshot`, `SnapshotFromFS`, and `SnapshotFromPaths` as requested.

Updated the CLI and existing validator tests for the error-only API. The valid validator fixtures now declare the variants their rules use.

Verification passed: `go test ./internal/cue ./internal/storage/fs ./internal/ext ./cmd/flipt`.
