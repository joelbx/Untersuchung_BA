Added `LogConfig.GRPCLevel` with the `grpc_level` JSON key, defaulted it to `"ERROR"`, and taught `Load` to read `log.grpc_level`. The config test fixture verifies a custom value while preserving the existing logging settings.

Verification: `go test ./config` and `git diff --check` passed.

Changed: [config.go](/app/config/config.go:34), [config_test.go](/app/config/config_test.go:238), [advanced.yml](/app/config/testdata/advanced.yml:1).