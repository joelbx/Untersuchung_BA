Added `LogConfig.GRPCLevel` with an `ERROR` default. `Load` now reads `log.grpc_level` independently of the existing logging settings.

The config tests and `git diff --check` pass. The full Go suite could not pass because the Redis tests require an unavailable Docker daemon. Details are in [checkpoint.md](/app/.codex-role-output/checkpoint.md).