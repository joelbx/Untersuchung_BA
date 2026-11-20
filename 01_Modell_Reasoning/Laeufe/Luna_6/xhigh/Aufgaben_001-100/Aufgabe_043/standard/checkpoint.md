# Checkpoint

Task: Extract tracing resource, provider, and exporter construction from gRPC startup into `internal/tracing`, then wire provider/exporter shutdown into the gRPC server lifecycle.

Requirements being tracked:
- Build an environment-aware OpenTelemetry resource with Flipt service name/version.
- Provide an always-on tracer provider constructor.
- Support Jaeger, Zipkin, and OTLP exporters, including accepted OTLP endpoint schemes and configured headers; return exporter shutdown.
- Make exporter construction safe across repeated invocations and report unsupported exporters/endpoints clearly.
- Use the tracing package from gRPC startup and register shutdowns in the existing lifecycle sequence.

Implementation status:
- Added `internal/tracing` with environment-aware resource creation, always-on provider construction, and per-call Jaeger, Zipkin, and OTLP exporter construction.
- OTLP accepts HTTP, HTTPS, gRPC, and scheme-less `host:port` endpoints, passes configured headers, and validates malformed endpoints with contextual errors.
- Replaced server-local tracing construction with the tracing package and registered provider/exporter shutdown through the server lifecycle.
- Migrated the existing exporter test to the extracted API.

Verification: `go test ./internal/tracing ./internal/cmd` passed; `git diff --check` passed.
