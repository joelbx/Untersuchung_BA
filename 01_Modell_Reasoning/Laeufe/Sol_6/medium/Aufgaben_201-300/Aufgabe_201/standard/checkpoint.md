# Progress

- Implemented unified rule segment YAML handling, canonical object export, and single-key operator fallback across import, snapshots, and SQL storage.
- Updated requested fixtures and added parsing/import coverage.
- Verified with `go test ./internal/ext ./internal/storage/fs ./internal/storage/sql` and `git diff --check`.
