Implemented `Load(path string) (*Result, error)` with configuration and warnings returned separately. Deprecation warnings are collected from keys explicitly present in the config file before defaults are applied, including `ui.enabled`. The CLI now logs warnings from `Result`.

Verification passed: `go test ./internal/config ./cmd/flipt` and `git diff --check`.