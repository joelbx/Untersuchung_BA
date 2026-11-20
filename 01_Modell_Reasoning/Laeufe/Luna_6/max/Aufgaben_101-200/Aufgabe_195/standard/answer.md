Implemented `Load(path) (*Result, error)` and moved warnings out of `Config`. Deprecations are collected before defaults and only when keys appear in the config file, including `ui.enabled`. The CLI now logs warnings from the result.

Verification passed: `go test ./internal/config ./cmd/flipt` and `git diff --check`.

See [config.go](/app/internal/config/config.go:25), [ui.go](/app/internal/config/ui.go:21), and [main.go](/app/cmd/flipt/main.go:163).