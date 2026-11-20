Implemented the tracing extraction in [tracing.go](/app/internal/tracing/tracing.go). It builds an environment-aware resource and always-sampling provider, and creates independent Jaeger, Zipkin, or OTLP exporters with shutdown functions. OTLP accepts the requested endpoint formats, applies configured headers, and reports invalid endpoints clearly.

[gRPC startup](/app/internal/cmd/grpc.go:154) now uses the tracing package and registers provider and exporter shutdowns in the server lifecycle. The existing exporter test now calls the extracted API.

Verification passed: `go test ./internal/tracing ./internal/cmd`; `git diff --check` passed.