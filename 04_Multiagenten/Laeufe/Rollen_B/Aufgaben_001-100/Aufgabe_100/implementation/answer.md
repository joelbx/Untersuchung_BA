Added `LogConfig.GRPCLevel` with an `"ERROR"` default. `Load(path)` now reads `log.grpc_level` independently of the existing logging settings.

Updated the config tests to cover the default and an explicit value. `go test ./config` and `git diff --check` pass.