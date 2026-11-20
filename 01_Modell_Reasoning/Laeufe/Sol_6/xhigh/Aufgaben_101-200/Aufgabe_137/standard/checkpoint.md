# Checkpoint

Task: add tracing sampling ratio and configurable propagators to repository configuration.

Status: implemented configuration defaults, validation, schema documentation, sampler and propagator wiring, and focused tests. Relevant suites pass with `GOPROXY=off GOSUMDB=off go test ./internal/config ./internal/tracing ./internal/cmd -count=1`. Final diff review remains.
