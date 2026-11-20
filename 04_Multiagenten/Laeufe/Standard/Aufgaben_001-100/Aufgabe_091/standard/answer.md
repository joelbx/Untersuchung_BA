Added `isoneof` and `isnotoneof` for string and numeric constraints, including JSON array type checks and the 100-item limit on create and update requests. Added focused tests for matching, invalid arrays, and the size boundary.

`go test ./rpc/flipt ./internal/server/evaluation` passes.