BatchEvaluate now returns one response per input flag in order, including disabled flags with `match: false` and an empty value. It continues after `ErrDisabled`, still aborts on other errors, and records a timestamp and per-flag duration alongside the total batch duration.

The protobuf message and gRPC code now use `timestamppb` and `emptypb`; empty-result RPCs return `*emptypb.Empty`. The generated gRPC gateway still uses the legacy protobuf interface required by the repository’s gateway v1 runtime.

Verification: `GOPROXY=off GOSUMDB=off GOFLAGS=-mod=mod go test ./... && git diff --check` passed.