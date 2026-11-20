Updated `config.Load` to return a `Result` containing separate `Config` and `Warnings` fields. Deprecation warnings now come from keys explicitly present in the configuration file, before defaults are applied, including `ui.enabled`. The CLI now logs warnings from the result.

`go test ./internal/config ./cmd/flipt` and `git diff --check` passed.