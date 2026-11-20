Added `LogConfig.GRPCLevel` with an `"ERROR"` default. `Load(path)` now reads `log.grpc_level` when provided, independently of the existing logging settings.

The existing config tests cover the default and an explicit value. `go test ./config` passed.