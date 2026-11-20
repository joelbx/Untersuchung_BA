Implemented `isoneof` and `isnotoneof` for string and numeric constraints, including operator recognition and create/update validation for correctly typed JSON arrays of up to 100 items.

Both existing test packages pass:

- `go test ./internal/server/evaluation`
- `cd rpc/flipt && go test .`

`git diff --check` is clean. See [legacy_evaluator.go](/app/internal/server/evaluation/legacy_evaluator.go:313), [operators.go](/app/rpc/flipt/operators.go:18), and [validation.go](/app/rpc/flipt/validation.go:42).