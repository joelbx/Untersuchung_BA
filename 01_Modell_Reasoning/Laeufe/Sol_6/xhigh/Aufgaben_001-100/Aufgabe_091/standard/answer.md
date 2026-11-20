Added `isoneof` and `isnotoneof` for string and number constraints. Create and update validation now rejects invalid or wrong-type JSON arrays and arrays over 100 items. Added tests for matching, validation errors, and the size limit.

The relevant test suites pass: `go test ./rpc/flipt ./internal/server/evaluation` with network fetching disabled.