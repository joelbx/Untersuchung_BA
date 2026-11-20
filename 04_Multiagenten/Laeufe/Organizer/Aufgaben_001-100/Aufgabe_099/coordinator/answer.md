BatchEvaluate now returns one response per input flag, in order, even when a flag is disabled. Disabled entries have `match: false` and an empty value; other evaluation errors still stop the batch. Each entry has its own timestamp and duration, and the outer response has the total duration.

Added `ErrDisabled` and `ErrDisabledf`, migrated timestamp and empty RPC types to `timestamppb` and `emptypb`, and added regression tests. `GOPROXY=off go test -mod=mod ./...` and `git diff --check` passed. No delegation was used.

The existing grpc-gateway v1 generated adapter still uses its legacy protobuf interface for compatibility.