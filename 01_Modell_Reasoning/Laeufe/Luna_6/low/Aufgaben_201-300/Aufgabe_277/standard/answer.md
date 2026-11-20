Implemented multi-segment audit data in [types.go](/app/internal/server/audit/types.go). `Rule` and `RolloutSegment` now include optional JSON operator fields, and their constructors join multiple segment keys and record the operator.

`go test ./internal/server/audit/...` passed, and `git diff --check` passed.