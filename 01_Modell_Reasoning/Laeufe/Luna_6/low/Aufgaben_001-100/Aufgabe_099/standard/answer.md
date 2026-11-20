Implemented the disabled flag handling. `ErrDisabled` and `ErrDisabledf` are defined in [errors.go](/app/errors/errors.go). Batch evaluation now continues after disabled flags, preserving input order and including a response with a timestamp and per flag duration for each input. Added a mixed enabled/disabled regression test in [evaluator_test.go](/app/server/evaluator_test.go).

Server timestamps now use `timestamppb`, and empty RPC results use `emptypb.Empty`.

Verification: `GOPROXY=off go test -mod=mod ./server ./rpc` passed. I restored `go.sum` after the command updated it.