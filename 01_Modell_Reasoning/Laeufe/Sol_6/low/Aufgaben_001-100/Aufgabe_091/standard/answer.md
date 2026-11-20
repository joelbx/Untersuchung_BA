Implemented `isoneof` and `isnotoneof` for string and number constraints. Create and update validation now checks JSON array types and enforces the 100-item limit. Added focused tests for evaluation and validation.

`go test ./rpc/flipt ./internal/server/evaluation` passed.