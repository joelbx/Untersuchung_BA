Task: add `log.grpc_level` to runtime configuration with an `ERROR` default.
Status: implemented `GRPCLevel` with `ERROR` default and `log.grpc_level` loading; updated config example and tests.
Verification: `GOPROXY=off GOSUMDB=off go test ./config ./cmd/flipt` passed.
