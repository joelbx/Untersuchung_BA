# Checkpoint

Implemented startup release handling in `internal/release`: prerelease detection covers dev, snapshot, and rc identifiers; update checking returns current/latest versions, availability, and release URL, and warns on request failure. Startup consumes this information for mode-specific output and `info.Flipt`, and disables telemetry for CI or non-release builds.

Verification: `go test ./internal/release ./internal/info ./cmd/flipt` passed; `git diff --check` passed.
