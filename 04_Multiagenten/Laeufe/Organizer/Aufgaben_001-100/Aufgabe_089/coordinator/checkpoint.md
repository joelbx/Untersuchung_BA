# Checkpoint

Completed: CUE validation now returns a multi-error with positioned schema and reference issues; CLI renders its individual errors. Import checks references before any writes, so retries report the same missing reference. Filesystem snapshot constructors validate references before assembly and expose StoreSnapshot, SnapshotFromFS, and SnapshotFromPaths. Corrected the three valid CUE fixtures to contain their referenced variants and added regression tests.

Verification: go test ./internal/storage/fs/... ./internal/cue ./internal/ext ./cmd/flipt passed; targeted package tests passed again after fixture edits; git diff --check passed. No delegation used.
