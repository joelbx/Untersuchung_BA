Added `LogConfig.GRPCLevel` with a default of `ERROR`, and taught `Load(path)` to read `log.grpc_level`. Extended the advanced config test to verify the configured value alongside the existing logging settings.

Validation passed: `go test ./config`.