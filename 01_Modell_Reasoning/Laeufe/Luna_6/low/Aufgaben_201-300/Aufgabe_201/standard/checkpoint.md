# Checkpoint

Issue: Support both string and object forms of the rule `segment` field.

Implemented:
- Added `IsSegment`, `SegmentKey`, `Segments`, and `SegmentEmbed` with YAML string/object conversion and validation.
- Unified `Rule` to one `segment` field. One-key object forms normalize to a key and OR operator.
- Updated rule importer, canonical object exporter, and filesystem snapshot conversion.
- Updated export fixture and requested readonly fixture rule examples; added focused wrapper tests.

Verification:
- `go test ./internal/ext ./internal/storage/fs ./internal/storage/sql/...` passed.

Known scope: SQL common persistence continues to use its existing protobuf key/operator representation; its focused SQL tests pass with the unchanged storage API.
