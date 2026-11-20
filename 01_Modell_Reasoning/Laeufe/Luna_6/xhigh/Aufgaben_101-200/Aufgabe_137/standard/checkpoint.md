# Checkpoint

Issue: add configurable tracing sampling ratio and context propagators.

Completed: added a validated sampling ratio and typed propagator options, supplied defaults in both config loading and `Default()`, wired the ratio sampler and propagator selection into runtime tracing, and updated the config schema and existing load fixture.

Verification: `GOPROXY=off GOSUMDB=off go test ./internal/config ./internal/tracing` and `GOPROXY=off GOSUMDB=off go test ./internal/cmd` pass. Offline `go mod tidy` could not resolve unrelated uncached modules; no network was used.
