Implemented tracing setup in [tracing.go](/app/internal/tracing/tracing.go): resource and provider creation are isolated from the server, and exporter setup supports Jaeger, Zipkin, and OTLP with headers, endpoint validation, and per invocation shutdown.

Updated gRPC startup to register provider and exporter shutdown in its lifecycle, and removed the shared exporter `sync.Once` state.

Verification passed: `go test ./internal/tracing ./internal/cmd` and `git diff --check`.