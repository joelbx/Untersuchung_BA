Added `LogConfig.GRPCLevel` with an `ERROR` default. `Load(path)` now reads `log.grpc_level` independently of the existing logging settings, and the sample config shows the new key. Tests cover the default and an explicit value.

Verification: `go test ./config` passed.