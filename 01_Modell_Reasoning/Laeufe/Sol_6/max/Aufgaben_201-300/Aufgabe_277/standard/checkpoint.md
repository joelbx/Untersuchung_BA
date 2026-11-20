# Rollout audit segment fields

Status: complete. Added `Rule.SegmentOperator` and `RolloutSegment.Operator` with optional JSON tags. The audit constructors now use the current segment key lists, join multiple keys, and record the operator name for multiple segments. Legacy segment keys remain supported when the list is empty.

Verification: `GOTOOLCHAIN=local GOPROXY=off GOSUMDB=off go test ./internal/server/audit/...` passed. Added JSON behavior tests for legacy, single, and multiple segments. Restored the test-generated `go.work.sum` change.
