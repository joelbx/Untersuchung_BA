Completed the repository change. Rule segments now accept a string or a keys/operator object, with single-key segments normalized to OR. Import, export, snapshot, SQL persistence, fixtures, and tests were updated.

Validation passed: `go test ./internal/ext ./internal/storage/fs ./internal/storage/sql/...` and `git diff --check`.