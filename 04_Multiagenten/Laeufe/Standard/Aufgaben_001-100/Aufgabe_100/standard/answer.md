Added `LogConfig.GRPCLevel` with an `ERROR` default. `Load(path)` now reads `log.grpc_level` independently of the existing logging settings. The default config example and tests cover both omitted and configured values.

Verification: `go test ./config` passed.