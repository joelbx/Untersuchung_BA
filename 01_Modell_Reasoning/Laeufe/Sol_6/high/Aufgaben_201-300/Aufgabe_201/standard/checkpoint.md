# Checkpoint

Completed unified rule segment YAML handling for string and keys/operator object formats. Importer, exporter, filesystem snapshot, and SQL rule/rollout persistence now normalize a single key to OR. Updated requested fixtures and added focused YAML, snapshot, and SQL coverage. Verified with `go test ./internal/ext ./internal/storage/fs ./internal/storage/sql` and `git diff --check`.
