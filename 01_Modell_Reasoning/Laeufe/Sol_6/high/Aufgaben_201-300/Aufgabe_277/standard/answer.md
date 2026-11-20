Updated [types.go](/app/internal/server/audit/types.go) so rule and rollout audit records include the optional operator fields. The constructors copy a single segment key, join multiple keys with commas and record the operator, while preserving the legacy key fallback. Added coverage in [types_test.go](/app/internal/server/audit/types_test.go).

`go test ./internal/server/audit/...` passed.