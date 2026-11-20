Task: Add configurable gRPC logging level to application config.
Found: LogConfig, Default(), and Load() are in config/config.go; existing config tests in config/config_test.go.
Completed: Added GRPCLevel with ERROR default and log.grpc_level load handling. Advanced fixture verifies explicit DEBUG; default assertion verifies ERROR.
Verification: go test ./config passed; git diff --check passed.
