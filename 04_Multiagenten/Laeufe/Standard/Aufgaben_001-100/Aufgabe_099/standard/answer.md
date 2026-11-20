BatchEvaluate now returns one ordered response per flag, including disabled flags with `match=false` and `value="disabled"`. It continues past disabled flags, still aborts on other errors, and records a timestamp and per-flag duration alongside the batch’s total duration.

Added `ErrDisabled` and `ErrDisabledf`, migrated protobuf timestamps and empty RPC results to `timestamppb` and `emptypb`, and added regression tests. The generated grpc-gateway v1 bridge still uses its required legacy proto interface.

Relevant server, RPC, and storage tests passed with network access disabled.