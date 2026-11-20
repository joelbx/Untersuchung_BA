Implemented tracing setup in [internal/tracing/tracing.go](/app/internal/tracing/tracing.go) and updated gRPC startup in [grpc.go](/app/internal/cmd/grpc.go) to use the new provider and exporter APIs, with shutdown callbacks registered in the server lifecycle.

`GetExporter` supports Jaeger, Zipkin, and OTLP; validates OTLP endpoints, applies configured headers, and provides an idempotent shutdown callback. The checkpoint is recorded in `.codex-role-output/checkpoint.md`.

Verification passed: `go test ./internal/tracing ./internal/cmd` and `git diff --check`.