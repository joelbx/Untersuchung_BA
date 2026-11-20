# Checkpoint

Task: support rule `segment` as a string or a keys/operator object throughout configuration, import/export, filesystem snapshots, and SQL persistence.

Root cause: `ext.Rule` split segment data across `SegmentKey`, `SegmentKeys`, and `SegmentOperator`. The `segment` YAML field was a string, so object input could not be decoded; importer and snapshot code read the split fields. SQL already stores multiple segment references and an operator, but did not normalize single-key operators consistently.

Changes: added `IsSegment`, `SegmentKey`, `Segments`, and `SegmentEmbed` with strict YAML decoding and marshaling for YAML v2/v3; replaced the split rule fields with one `Segment`; normalized single-key segments to OR; updated importer, canonical object export, snapshot extraction, and SQL rule/rollout read/write paths. Updated requested fixtures and added focused tests.

Verification: `go test ./internal/ext ./internal/storage/fs ./internal/storage/sql -count=1` passed (exit 0). `git diff --check` passed (exit 0). Initial failing reproduction: `go test ./internal/ext -run TestRuleSegmentForms -count=1` failed because `Rule.Segment` did not exist. A later YAML v3 reproduction failed on `map[string]interface{}` before the decoder fix. No downloads were made.
