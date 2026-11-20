Implemented support for string and `{keys, operator}` rule segments, including strict YAML validation, single-key OR fallback, and canonical object-form rule exports. Import, filesystem snapshots, and SQL rule/rollout persistence now handle the normalized segment data.

Updated the requested export and readonly fixtures, and added the supplied multi-segment import fixture.

Verification passed: `go test ./internal/ext ./internal/storage/fs ./internal/storage/sql`, `go test ./internal/storage/sql/...`, and `git diff --check`.