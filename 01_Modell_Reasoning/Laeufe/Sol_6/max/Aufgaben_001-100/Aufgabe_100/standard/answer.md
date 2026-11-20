Added `LogConfig.GRPCLevel` in [config.go](/app/config/config.go). `Default()` sets it to `ERROR`, and `Load(path)` reads `log.grpc_level` when provided. The existing logging fields retain their behavior.

Updated the example and advanced config fixture. `go test ./config` and `git diff --check` passed.