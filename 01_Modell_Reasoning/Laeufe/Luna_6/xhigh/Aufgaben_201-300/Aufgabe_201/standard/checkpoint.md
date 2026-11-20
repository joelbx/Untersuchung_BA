# Checkpoint

Task: Support `rules[].segment` as either a string key or a keys/operator object, with canonical object export and backward compatibility.

Completed:
- Added `SegmentEmbed`, `IsSegment`, `SegmentKey`, and `Segments` with strict YAML decoding, YAML encoding, and single-key OR normalization.
- Consolidated `ext.Rule` segment config into `Segment` and retained decoding for the previous sibling `segments`/`operator` syntax.
- Updated importer, exporter, filesystem snapshots, and SQL rule/rollout/evaluation paths to carry keys and operators and enforce single-key OR.
- Updated export and readonly fixtures and added `import_rule_multiple_segments.yml`.

Validation:
- `go test ./internal/ext ./internal/storage/fs ./internal/storage/sql` passed.
- `git diff --check` passed.
