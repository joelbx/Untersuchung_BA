Added `isoneof` and `isnotoneof` for string and number constraints. Create and update validation now checks JSON array types and enforces the 100 item limit. Added tests for matching, invalid values, and the size boundary.

`go test ./rpc/flipt ./internal/server/evaluation` and `git diff --check` passed.