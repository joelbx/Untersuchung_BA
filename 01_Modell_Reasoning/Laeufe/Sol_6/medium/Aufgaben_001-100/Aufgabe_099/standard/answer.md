Fixed `BatchEvaluate` so disabled flags produce an entry in input order with `match: false`, an empty value, a timestamp, and their own request duration. Other evaluation errors still abort the batch, and the outer response retains the total duration.

Added `ErrDisabled` and `ErrDisabledf`, migrated timestamp and empty-result types to `timestamppb` and `emptypb`, and kept the grpc-gateway v1 legacy proto import required by its forwarding API.

Verification: `GOPROXY=off GOSUMDB=off go test -mod=mod ./...` passed.