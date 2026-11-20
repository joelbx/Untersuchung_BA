Implemented the audit segment fields and constructor handling in [types.go](/app/internal/server/audit/types.go:136). Single segments use their key; multiple segment keys are comma-joined and include the operator name.

`go test ./internal/server/audit/...` passed.