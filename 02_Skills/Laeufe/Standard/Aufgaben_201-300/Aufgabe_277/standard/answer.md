Updated rollout audit data so `Rule` and `RolloutSegment` expose optional operator fields. Their constructors now copy single segment keys and join multiple keys with commas, recording the operator for multi-segment entries. Rollout segment values are preserved.

Added regression tests for legacy, single, and multiple segments. `go test ./internal/server/audit/...` and `git diff --check` passed.