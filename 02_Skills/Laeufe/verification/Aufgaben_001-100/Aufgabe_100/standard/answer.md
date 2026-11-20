Added `LogConfig.GRPCLevel` with a default of `"ERROR"`. `Load(path)` now reads `log.grpc_level` when provided, independently of the existing log settings. Updated the sample config and tests.

Verification: `GOPROXY=off go test ./config -count=1` and `git diff --check` passed.