Task: add a configurable gRPC logging level to application configuration.
Plan: inspect config definitions and loader, update the default and load path, then run existing relevant tests.
Status: complete. Added LogConfig.GRPCLevel with ERROR default, loaded log.grpc_level independently, documented the default, and updated existing config coverage. Verified with `go test ./config` and `git diff --check`.
