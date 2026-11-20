# Checkpoint

Task: separate configuration warnings from Config via Load Result; warn for explicitly present deprecated file keys including ui.enabled.

Implemented: `Result{Config, Warnings}`; warning collection occurs after reading the file and before defaults. The CLI logs warnings from Result. Existing deprecations inspect file presence, including false values, and `ui.enabled` has a warning.

TDD: `GOTOOLCHAIN=local GOPROXY=off go test ./internal/config -run '^TestLoadReturnsConfigurationAndFileDeprecationsSeparately$' -count=1` failed as expected because Load had no Result.Config field. After implementation, `GOTOOLCHAIN=local GOPROXY=off go test ./internal/config -count=1` passed. Full `go test ./...` pending.

Full suite: `GOTOOLCHAIN=local GOPROXY=off go test ./...` exited 1. `internal/config` passed, but `internal/server/cache/redis` failed `TestSet`, `TestGet`, and `TestDelete`: `Cannot connect to the Docker daemon at unix:///var/run/docker.sock. Is the docker daemon running?: failed to create container`. Those integration tests remain unverified in this environment.
