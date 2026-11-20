Updated [types.go](/app/internal/server/audit/types.go) with optional operator fields and conversion of single or multiple segment keys. Multiple keys are comma-joined and include the operator name.

`go test ./internal/server/audit/...` and `git diff --check` passed.