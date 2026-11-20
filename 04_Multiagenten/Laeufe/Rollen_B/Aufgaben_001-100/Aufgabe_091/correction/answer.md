Fixed create and update validation so an empty value for `isoneof` or `isnotoneof` returns the required invalid-value error. Added regression cases for string and number lists with both operators.

The reviewer’s exact test command, `go test ./internal/server/evaluation ./rpc/flipt`, passes. `git diff --check` passes. No remaining failures or test environment problems.