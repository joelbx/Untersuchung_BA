Implemented the configuration refactor. `Load` now returns `Result` with separate `Config` and `Warnings` fields, and the CLI logs warnings from the result. Deprecation warnings are collected from keys explicitly present in the file before defaults are applied, including `ui.enabled`.

Updated the config tests. `go test ./internal/config ./cmd/flipt` passed, and `git diff --check` was clean.