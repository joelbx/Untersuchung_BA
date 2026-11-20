Implemented referential checks with location-aware, multi-unwrappable errors in [validate.go](/app/internal/cue/validate.go:63). Snapshot creation checks references before assembly, and imports check them before writing resources, so invalid imports fail consistently on repeated attempts.

Exported `StoreSnapshot`, `SnapshotFromFS`, and `SnapshotFromPaths` in [snapshot.go](/app/internal/storage/fs/snapshot.go:46), and updated the CLI for the error-only validation API.

Verification passed: `go test ./internal/cue ./internal/storage/fs ./internal/ext ./cmd/flipt`.