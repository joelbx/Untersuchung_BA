# Checkpoint

Task: extract tracing resource, provider, and exporter setup from the gRPC server into `internal/tracing`, preserve lifecycle shutdown, and verify with existing local tests.

Status: complete.

Implementation: added `internal/tracing/tracing.go` with resource creation, always-on provider, exporter construction, OTLP endpoint validation, and a shared one-time shutdown wrapper. Updated gRPC startup to use the package and removed the old package-level exporter singleton. Moved exporter tests into `internal/tracing` and added isolated resource, sampling, error, repeated-call, HTTP header/path, and shutdown coverage. Enabled tracing in the gRPC server lifecycle test.

Verification: `GOPROXY=off GOSUMDB=off go test ./internal/tracing ./internal/cmd` passed; `git diff --check` passed.
