VERDICT: FIX

Code defect: `CreateConstraintRequest.Validate` and `UpdateConstraintRequest.Validate` return `errors.EmptyFieldError("value")` for an empty value before calling `validateArrayValue` for `isoneof` or `isnotoneof` (`rpc/flipt/validation.go:447-453,509-515`). The requirement says list operators always call the helper, which would produce `invalid value provided for property "<property>" of type string/number` for empty, invalid JSON. Move the list-operator check ahead of the empty-value branch in both methods.

Tests: `go test ./internal/server/evaluation ./rpc/flipt` passed (`ok` for both packages). Existing list tests omit empty constraint values, so this defect is not covered. No TEST_ENVIRONMENT_PROBLEM. Go test changed `go.work.sum` as a side effect; restored it to its initial state. Project code was not edited during review.
