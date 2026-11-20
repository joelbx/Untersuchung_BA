Implemented `isoneof` and `isnotoneof` for string and number constraints, including operator registration and create/update validation for JSON arrays of up to 100 items.

Verification passed: `go test ./internal/server/evaluation ./rpc/flipt` and `git diff --check`.