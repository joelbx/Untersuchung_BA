Added `LogConfig.GRPCLevel` with an `ERROR` default. `Load(path)` now reads `log.grpc_level` independently of the existing logging fields. The default config example and tests were updated.

Verified with `go test ./config` and `git diff --check`; both passed.