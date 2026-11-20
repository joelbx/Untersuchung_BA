Added tracing configuration for `samplingRatio` and the supported propagators, with the requested defaults and exact validation errors. The tracer now uses the configured sampling ratio, and gRPC uses the configured propagators. The schema and tests were updated.

Verification passed offline: `go test ./internal/config ./internal/tracing ./internal/cmd` and `git diff --check`.