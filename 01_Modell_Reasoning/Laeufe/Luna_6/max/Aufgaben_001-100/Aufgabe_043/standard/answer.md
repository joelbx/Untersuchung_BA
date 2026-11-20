Implemented tracing extraction in [tracing.go](/app/internal/tracing/tracing.go): it builds the environment-aware resource and always-on provider, and creates Jaeger, Zipkin, or OTLP exporters with endpoint validation and idempotent shutdown.

[gRPC startup](/app/internal/cmd/grpc.go) now uses these APIs and registers exporter and provider shutdowns. Updated the exporter test to use the new package API.

Verification passed: `go test ./internal/tracing ./internal/cmd` and `git diff --check`.