Added `isoneof` and `isnotoneof` for string and number constraints. Create and update validation now checks JSON array types and enforces the 100 item limit. Added tests for membership, invalid values, and the size boundary.

Verified with `go test ./rpc/flipt ./internal/server/evaluation ./internal/server` and `git diff --check`; all passed.