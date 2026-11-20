Implemented `isoneof` and `isnotoneof` for string and number constraints. Create and update validation now checks that values are JSON arrays of the correct type with at most 100 items; focused tests cover matching and invalid lists.

Verified with `go test ./rpc/flipt ./internal/server/evaluation` and `git diff --check`.