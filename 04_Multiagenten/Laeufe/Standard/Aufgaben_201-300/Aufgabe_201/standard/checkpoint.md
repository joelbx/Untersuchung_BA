Task: Support string and object segment formats in rules configuration.
Status: Complete.
Implemented: unified SegmentEmbed/IsSegment YAML model, importer/exporter and filesystem snapshot handling, SQL rule/rollout single-key OR fallback, requested fixtures, focused tests.
Verification: go test ./internal/ext ./internal/storage/fs ./internal/storage/sql (pass); git diff --check (pass).
