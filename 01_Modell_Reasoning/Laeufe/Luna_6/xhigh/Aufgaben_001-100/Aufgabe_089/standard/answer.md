Implemented referential validation for unknown variants and segments, with individual errors formatted as `message (file line:column)` and available through `cue.Unwrap`.

Exported `StoreSnapshot`, `SnapshotFromFS`, and `SnapshotFromPaths`; both snapshot constructors validate inputs. Updated `flipt validate` to display individual errors and `flipt import` to validate before changing storage.

Verification passed: `go test ./internal/cue ./internal/storage/fs ./internal/ext ./cmd/flipt`; `git diff --check` is clean.