Added `LogConfig.GRPCLevel`, defaulting to `ERROR`, and wired `log.grpc_level` into `Load()` independently of the existing logging settings.

Updated the advanced config fixture to verify a custom value. `go test ./config` and `git diff --check` pass.