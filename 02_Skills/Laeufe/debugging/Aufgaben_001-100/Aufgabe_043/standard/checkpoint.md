# Checkpoint

Issue: Extract tracing provider/resource/exporter setup from `internal/cmd/grpc.go` into `internal/tracing`.

Status: Investigating current implementation and tests. No code changes yet.

Tooling: `rg` is unavailable (`/bin/bash: rg: command not found`); using `find` and `grep` for local searches.

Investigation: `grpc.go` built the resource/provider and all exporters inline. `getTraceExporter` used package-level `sync.Once`, so its first configuration and error were reused for later calls. Existing `grpc_test.go` reset that global between subtests, confirming the coupling. The current resource used `WithAttributes` and `WithFromEnv`; exporter branches support Jaeger, Zipkin, and OTLP.

Reproduction: Added isolated tracing tests and ran `GOTOOLCHAIN=local GOPROXY=off go test ./internal/tracing -run 'TestNewResource|TestNewProvider|TestGetExporter' -count=1`; it failed as expected with undefined `newResource`, `NewProvider`, and `GetExporter`.

Patch: New `internal/tracing` package provides resource, provider, and per-call exporter initialization. `grpc.go` delegates and registers shutdown; former exporter test moved to isolated package and expanded. `GOTOOLCHAIN=local GOPROXY=off go test ./internal/tracing -count=1` passed. Server test is running.

Final verification:
- `GOTOOLCHAIN=local GOPROXY=off go test ./internal/tracing -count=1` passed, including resource overrides, sampler, repeated exporter calls, OTLP endpoint variants, malformed/unsupported values, and HTTP header/path export.
- `GOTOOLCHAIN=local GOPROXY=off go test ./internal/cmd -run 'TestNewGRPCServer' -count=1` passed.
- `GOTOOLCHAIN=local GOPROXY=off go test ./internal/cmd -count=1` passed.
- `git diff --check` passed.

No external research or downloads were used. The server's provider shutdown remains registered after span processors so reverse shutdown order is preserved.
