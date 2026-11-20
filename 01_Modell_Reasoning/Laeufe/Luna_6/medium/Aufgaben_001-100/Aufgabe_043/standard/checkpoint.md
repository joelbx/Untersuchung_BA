# Checkpoint

Implemented tracing extraction in `internal/tracing/tracing.go`:
- resource creation includes Flipt service name/version and OpenTelemetry environment attributes;
- provider uses always-on sampling;
- exporter construction supports Jaeger, Zipkin, OTLP HTTP(S), OTLP gRPC, and scheme-less host:port, with configured OTLP headers and exporter shutdown;
- each invocation owns independent exporter state, and unsupported exporters / invalid endpoints return descriptive errors.

Updated gRPC startup to use `tracing.NewProvider` and `tracing.GetExporter`, registering exporter and provider shutdown in the server cleanup stack. Removed the old exporter global `sync.Once` state and adjusted its existing test accordingly.

Verification: `go test ./internal/tracing ./internal/cmd` passed; `git diff --check` passed.
