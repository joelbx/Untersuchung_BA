BatchEvaluate now returns one result per input flag in order, including disabled flags with `match: false` and no value. Disabled flags no longer abort the batch. Each entry has a timestamp and its own duration; the outer response has the total duration.

Added `ErrDisabled` and `ErrDisabledf`, and migrated protobuf and gRPC types plus empty-result RPCs to `timestamppb` and `emptypb`. Regression tests and the full Go suite pass with `GOPROXY=off go test -mod=mod ./... -count=1`.

The generated gateway v1 file still uses its runtime’s legacy protobuf interface. That remaining migration is recorded in the [checkpoint](/app/.codex-role-output/checkpoint.md).