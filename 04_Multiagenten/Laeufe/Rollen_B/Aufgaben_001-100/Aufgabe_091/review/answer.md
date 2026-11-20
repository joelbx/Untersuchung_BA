VERDICT: FIX

Both create and update validation return a generic empty-value error before calling `validateArrayValue` for `isoneof` and `isnotoneof` ([validation.go](/app/rpc/flipt/validation.go:447), [update path](/app/rpc/flipt/validation.go:509)). Move the list-operator check ahead of the empty-value check in both methods so empty JSON input receives the required invalid-value error.

`go test ./internal/server/evaluation ./rpc/flipt` passed for both packages. The existing tests do not cover an empty list value. No TEST_ENVIRONMENT_PROBLEM. I made no project code changes during this independent review.