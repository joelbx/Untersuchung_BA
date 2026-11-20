# Checkpoint

Issue: add an independent configurable gRPC logging level to application configuration.

Implemented:
- Added `LogConfig.GRPCLevel` with the `grpc_level` JSON key.
- Set `GRPCLevel` to `ERROR` in `Default()`.
- Added optional `log.grpc_level` loading.
- Documented the default in `config/default.yml` and extended the existing advanced config fixture and expectation with `DEBUG`.

Validation:
- `gofmt -w config/config.go config/config_test.go` passed.
- `git diff --check` passed.
- `go test ./config` passed.
