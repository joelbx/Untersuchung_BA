# Checkpoint

Status: implementation complete; targeted tests passed.

Changes:
- Added `internal/tracing` resource, provider, and exporter APIs.
- Added OTLP endpoint validation/support for HTTP, HTTPS, gRPC, and scheme-less host:port endpoints; configured headers are passed through.
- Made exporter shutdown idempotent per exporter and removed the process-wide exporter cache.
- Updated gRPC initialization and its exporter test to use the extracted tracing API.

Verification: `go test ./internal/tracing ./internal/cmd` passed. `git diff --check` passed.

Constraints: work from checked-out repository code only; no git history, index baseline, or harness configuration changes.
