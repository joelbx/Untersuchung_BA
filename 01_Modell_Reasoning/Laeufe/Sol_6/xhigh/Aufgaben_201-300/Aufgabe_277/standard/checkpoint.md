# Rollout audit fields

Status: complete. Added optional operator fields to the audit Rule and RolloutSegment structures. Constructors use the listed segment keys when present, join multiple keys with commas, and record the operator for multiple segments. Added tests for legacy, single, and multiple segment cases, both operator values, and JSON omission. `GOPROXY=off GOSUMDB=off go test ./internal/server/audit/...` passed. Restored the incidental `go.work.sum` update from the test command.
