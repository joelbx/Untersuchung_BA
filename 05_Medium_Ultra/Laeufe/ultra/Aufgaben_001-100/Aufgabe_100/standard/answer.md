Added `LogConfig.GRPCLevel` with an `ERROR` default and support for `log.grpc_level` in [config.go](/app/config/config.go:34). The updated config test verifies that a `DEBUG` override loads while the existing logging settings retain their values.

Two subagents reviewed the implementation and test coverage. `go test ./config`, `go test ./cmd/flipt` (compile check), and `git diff --check` passed.