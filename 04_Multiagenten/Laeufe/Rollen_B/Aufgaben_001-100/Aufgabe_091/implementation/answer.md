Implemented `isoneof` and `isnotoneof` for string and number constraints. Create and update validation now checks JSON array types, rejects null elements, and enforces the 100 item limit. Added focused tests for matching, invalid lists, and the size boundary.

The local tests passed: `go test ./rpc/flipt ./internal/server/evaluation`.