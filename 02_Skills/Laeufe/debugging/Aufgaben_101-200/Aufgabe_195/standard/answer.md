Updated `Load` to return a `Result` with separate `Config` and `Warnings` fields. Deprecation warnings now depend on keys explicitly present in the configuration file, including `ui.enabled`, and the CLI logs warnings from the result.

Verification passed: `GOPROXY=off go test ./internal/config ./cmd/flipt -count=1` and `git diff --check`.