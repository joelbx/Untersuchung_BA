Added `LogConfig.GRPCLevel` with an `ERROR` default and made `Load(path)` read `log.grpc_level`. The existing logging fields remain unchanged. Updated the sample config and tests to cover the default and an explicit gRPC level.

`go test ./config ./cmd/flipt` and `git diff --check` passed.