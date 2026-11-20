Implemented the tracing extraction in [tracing.go](/app/internal/tracing/tracing.go). It provides resource creation with OTEL environment attributes, an always-on provider, and Jaeger, Zipkin, and OTLP exporters with endpoint validation and shutdown functions.

Updated [grpc.go](/app/internal/cmd/grpc.go) to use the new APIs and register provider and exporter shutdowns in the server lifecycle. Updated the existing exporter test to call the new API.

Verification: `go test ./internal/tracing ./internal/cmd` passed, and `git diff --check` passed.