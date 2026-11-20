Fixed `BatchEvaluate` so disabled flags produce entries in input order with `match=false`, a disabled message in `value`, a timestamp, and their own duration. The batch still aborts on other errors and reports its total duration.

Added `ErrDisabled` and `ErrDisabledf`, migrated protobuf timestamp and empty result types, and preserved the single flag RPC’s error status. The generated gateway retains its legacy protobuf import because the repository’s grpc-gateway v1 runtime requires it.

Verification: `GOPROXY=off GOSUMDB=off go test -mod=mod ./...` passed.