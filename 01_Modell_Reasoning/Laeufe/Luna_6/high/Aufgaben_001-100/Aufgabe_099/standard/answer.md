Implemented the disabled flag handling in [evaluator.go](/app/server/evaluator.go): `ErrDisabled` is detected with `errors.As`, and batch evaluation continues with a `"DISABLED"` response entry in input order. Each entry gets its own timestamp and duration, while the outer response measures the full batch.

Added `ErrDisabled` and `ErrDisabledf`, and migrated RPC empty messages and timestamp handling to `emptypb` and `timestamppb`.

`gofmt`, `git diff --check`, and `go test ./errors` passed. The relevant server, storage, and RPC tests could not start because `go.sum` lacks required dependency entries; I did not attempt downloads.