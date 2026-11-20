Task: Refactor configuration loading to return Config and Warnings separately, and warn on explicit ui.enabled and other deprecated keys.
Status: Complete. Load returns *Result; deprecations are collected from file keys before defaults; CLI logs Result.Warnings. Existing configuration tests updated and new cases cover false cache.memory.enabled, standalone expiration, and true ui.enabled.
Verification: GOPROXY=off GOSUMDB=off go test ./internal/config (pass); GOPROXY=off GOSUMDB=off go test ./cmd/flipt (pass); git diff --check (pass).
