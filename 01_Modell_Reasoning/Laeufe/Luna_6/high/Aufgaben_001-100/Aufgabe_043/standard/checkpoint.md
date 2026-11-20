# Checkpoint

- Implemented `internal/tracing.newResource`, `NewProvider`, and `GetExporter` for Jaeger, Zipkin, and OTLP.
- OTLP accepts HTTP, HTTPS, gRPC, and validated scheme-less host:port endpoints; configured headers are passed through, HTTP/HTTPS behavior is preserved, and shutdown is safe to call repeatedly.
- gRPC startup now uses the tracing APIs and registers exporter and provider shutdowns in its existing reverse-order shutdown lifecycle.
- Verification passed: `go test ./internal/tracing ./internal/cmd`; `git diff --check` clean.
