# Checkpoint

Task: Separate configuration warnings from Config using Result, and warn when deprecated keys are explicitly set, including ui.enabled.
Status: Complete. Loader returns Result with Config and Warnings; deprecations inspect file keys before defaults; CLI logs warnings on load; tests cover explicit false, defaults, environment, and ui.enabled. `GOPROXY=off go test ./internal/config ./cmd/flipt` passes.
