# Checkpoint

Task: Add a dedicated gRPC logging level to application configuration.
Status: Complete.
Changes: `LogConfig.GRPCLevel` defaults to `ERROR`; `Load` reads `log.grpc_level`; config example and existing load tests cover the new setting.
Verification: `GOPROXY=off GOSUMDB=off go test ./config` passed; `git diff --check` passed.
