# Checkpoint

Implemented the audit segment fields and constructor behavior in `internal/server/audit/types.go`:

- `Rule.SegmentOperator` serializes as `segment_operator,omitempty`.
- `RolloutSegment.Operator` serializes as `operator,omitempty`.
- Rule and rollout segment constructors preserve a single key, or join multiple keys with commas and record the protobuf operator name.
- Added focused tests for single and multiple segment cases.

Verification: `go test ./internal/server/audit/...` passed.
