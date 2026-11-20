# Checkpoint

Task: Resolve the rollout audit log segment fields and constructor population issue.

Implemented in `internal/server/audit/types.go`:
- Added `Rule.SegmentOperator` with JSON tag `segment_operator,omitempty`.
- Added `RolloutSegment.Operator` with JSON tag `operator,omitempty`.
- Updated `NewRule` and `NewRollout` to use the single segment key when present, join multiple segment keys with commas, and include the operator name for multiple segments. Legacy `SegmentKey` remains the fallback when `SegmentKeys` is empty.

Verification: `go test ./internal/server/audit/...` passed for audit, kafka, log, template, and webhook packages.
