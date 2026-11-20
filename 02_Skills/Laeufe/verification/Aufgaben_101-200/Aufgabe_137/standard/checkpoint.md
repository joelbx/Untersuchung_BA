# Checkpoint

Task: add tracing sampling ratio and propagator configuration with defaults and validation.

Status: implementation complete; relevant workspace tests passed. `rg` is unavailable in this environment; using local shell alternatives.

Implemented:
- Tracing ratio and propagator fields, defaults, validation, and schema entries.
- Configured sampler and runtime propagator selection using locally cached OpenTelemetry modules.
- Tests for defaults, overrides, exact validation errors, and sampler boundaries.

Verification so far:
- `GOPROXY=off go test ./internal/config` passed (`ok go.flipt.io/flipt/internal/config 0.210s`).
- `GOPROXY=off GOSUMDB=off go test -mod=mod ./internal/config ./internal/tracing ./internal/cmd` failed: workspace mode only permits `-mod=readonly` or `vendor`.
- `GOWORK=off GOPROXY=off GOSUMDB=off go test -mod=mod ./internal/config ./internal/tracing ./internal/cmd` failed: missing cached versions of existing dependencies, including `golang.org/x/sync v0.6.0` (`module lookup disabled by GOPROXY=off`). This does not establish a code failure.
- `GOPROXY=off go test ./internal/config ./internal/tracing ./internal/cmd` passed: config 0.310s, tracing 0.020s, cmd cached.
- `git diff --check` passed with no output.

Remaining uncertainty: no full repository test suite was run; the relevant packages above passed offline in workspace mode.
