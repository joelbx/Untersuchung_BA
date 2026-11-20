Implemented disabled flag handling in BatchEvaluate. Disabled flags now return a typed `ErrDisabled` and an ordered response with `value: "disabled"`; each entry gets its own timestamp and duration, and the batch records total duration. See [errors.go](/app/errors/errors.go:37) and [evaluator.go](/app/server/evaluator.go:66).

Migrated protobuf timestamps and empty RPC results to `timestamppb` and `emptypb`, including storage helpers and generated RPC code.

Verification passed: `go test ./...` using a temporary modfile with `GOPROXY=off`, and `git diff --check`. The temporary modfile worked around missing baseline `go.sum` entries without changing repository checksum files.