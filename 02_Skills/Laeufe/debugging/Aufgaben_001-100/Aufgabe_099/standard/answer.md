Fixed `BatchEvaluate` so a disabled flag no longer aborts the batch. Results stay in input order; disabled entries have `match=false`, an empty value, a timestamp, and their own duration. The outer response retains the total duration.

Added `ErrDisabled` and `ErrDisabledf`, migrated generated protobuf and gRPC types to `timestamppb` and `emptypb`, and updated empty-result RPC methods.

Verification: `GOPROXY=off GOSUMDB=off go test -mod=mod ./...` passed.