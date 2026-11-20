Added `LogConfig.GRPCLevel` with an `ERROR` default. `Load(path)` now reads `log.grpc_level` independently of the existing logging settings. Updated the config example and tests.

Verification passed: `go test ./config ./cmd/flipt`.