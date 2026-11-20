# Checkpoint

Implemented unified rule `segment` YAML wrapper with string and keys/operator object support, strict invalid-format handling, single-key OR fallback, and canonical object export. Updated importer, filesystem snapshots, SQL rule/rollout persistence, requested fixtures, and focused tests.

Verification: `go test ./internal/ext ./internal/storage/fs ./internal/storage/sql/common ./internal/storage/sql` passed; `git diff --check` passed. No delegation used.
