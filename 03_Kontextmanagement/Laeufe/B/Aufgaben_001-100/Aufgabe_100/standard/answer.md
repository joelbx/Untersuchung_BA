Added `LogConfig.GRPCLevel` with an `"ERROR"` default. `Load(path)` now reads `log.grpc_level` independently of the existing logging settings. Updated the config test fixture to cover an explicit value.

Verified with `go test ./config` and `git diff --check`.