Added `LogConfig.GRPCLevel` with an `ERROR` default and made `Load(path)` read `log.grpc_level`. The existing logging fields retain their behavior. The advanced config test verifies a gRPC level of `DEBUG` alongside a global level of `WARN`.

`go test ./config` passes.