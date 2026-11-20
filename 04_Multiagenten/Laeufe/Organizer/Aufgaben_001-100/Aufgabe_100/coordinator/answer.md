Added `LogConfig.GRPCLevel` with an `ERROR` default. `Load(path)` now reads `log.grpc_level` independently of the existing log settings. Updated the sample config and tests for both the default and an explicit value.

`go test ./config` and `git diff --check` passed. No delegation was used.