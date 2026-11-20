Updated [Load](/app/internal/config/config.go) to return `*Result` with separate `Config` and `Warnings`. Deprecation warnings now come only from keys explicitly present in the configuration file, before defaults are applied. Added the `ui.enabled` warning and updated the CLI to log warnings from `Result`.

Verification passed: `go test ./internal/config ./cmd/flipt` and `git diff --check`.