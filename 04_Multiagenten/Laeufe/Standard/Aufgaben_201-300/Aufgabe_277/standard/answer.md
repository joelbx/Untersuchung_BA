Updated the audit types and constructors in [types.go](/app/internal/server/audit/types.go). Rules and rollouts now record a single segment key, or comma-separated keys and the operator for multiple segments. The new operator fields are omitted from JSON when empty.

Added coverage in [types_test.go](/app/internal/server/audit/types_test.go). `go test ./internal/server/audit/...` passed.