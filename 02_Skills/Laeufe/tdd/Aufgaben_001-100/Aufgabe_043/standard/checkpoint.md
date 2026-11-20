# Checkpoint

Task: Extract tracing provider/resource/exporter setup from gRPC startup into internal/tracing, with isolated tests and lifecycle shutdown.

TDD red: `go test ./internal/tracing` failed with undefined newResource, NewProvider, and GetExporter, as expected before implementation.

Implementation: new tracing package now builds resource/provider/exporters; gRPC startup calls it and registers provider/exporter shutdown. Existing exporter tests moved from cmd to tracing and expanded for environment and repeated invocation. `go test ./internal/tracing` passed.

Verification in progress: `go test ./internal/tracing ./internal/cmd` and `go test ./...` are running. No offline tooling issue observed.

Focused verification after final lifecycle ordering edit: `go test ./internal/tracing ./internal/cmd` passed. `git diff --check` passed.

Full suite `go test ./...` is still running. Observed failures so far:
- `internal/cache/redis`: TestSet, TestGet, TestDelete cannot connect to Docker daemon at unix:///var/run/docker.sock.
- `internal/gitfs`: Test_FS_Submodule attempts a GitHub URL and receives Forbidden (external research/network blocked).
These checks cannot be verified locally with the available services; the tracing-specific packages passed.

Full `go test ./...` completed with exit code 1. Failures observed: `internal/cache/redis` TestSet, TestGet, TestDelete (Docker daemon unavailable); `internal/gitfs` Test_FS_Submodule (GitHub request Forbidden). All other printed packages passed, including internal/tracing and internal/cmd. This limits full-suite verification but does not indicate a tracing regression.
