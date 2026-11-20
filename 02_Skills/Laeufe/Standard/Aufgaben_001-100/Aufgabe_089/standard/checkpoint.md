# Checkpoint

Implemented CUE validation errors with file, line, and column locations and local reference checks for rule variants and segments, including boolean flag rules and rollouts. Exported StoreSnapshot, SnapshotFromFS, and SnapshotFromPaths; snapshot construction checks references before loading. Import preflights rule references before writes so repeated attempts fail consistently. Corrected valid fixtures that referenced missing variants.

Verification: `GOPROXY=off GOSUMDB=off go test ./internal/cue ./internal/storage/fs ./internal/ext ./cmd/flipt` passed. `git diff --check` passed.
