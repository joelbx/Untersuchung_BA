Implemented `isoneof` and `isnotoneof` for string and number constraints, including strict JSON array validation and the 100 item limit for create and update requests.

Updated [operators.go](/app/rpc/flipt/operators.go), [validation.go](/app/rpc/flipt/validation.go), and [legacy_evaluator.go](/app/internal/server/evaluation/legacy_evaluator.go).

Verification passed: `go test ./rpc/flipt ./internal/server/evaluation` and `git diff --check`.