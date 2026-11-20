Updated `config.Load` to return a `Result` with separate `Config` and `Warnings` fields. Deprecation warnings now come from keys explicitly present in the config file, including `ui.enabled`, and the command logs them during initialization.

Verified with `GOPROXY=off go test ./internal/config ./cmd/flipt`.