# Checkpoint

Task: support string and structured forms for the rule `segment` field throughout configuration, import/export, snapshots, and SQL persistence.

Completed: added `SegmentEmbed`, `IsSegment`, `SegmentKey`, and `Segments` with YAML validation and single-key OR fallback; adapted importer/exporter, filesystem snapshot construction, and SQL rule/rollout persistence; updated the requested export and readonly integration fixtures and added the multiple-segment import fixture.

Verification: `go test ./internal/ext ./internal/storage/fs ./internal/storage/sql/...` passed. `git diff --check` passed.
