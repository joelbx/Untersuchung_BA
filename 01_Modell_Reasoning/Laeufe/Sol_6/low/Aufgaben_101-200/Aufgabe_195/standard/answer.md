Configuration loading now returns `(*Result, error)`, with `Config` and `Warnings` as separate fields. The loader collects deprecation warnings from keys explicitly present in the file before applying defaults, including `ui.enabled`. The CLI reads and logs warnings from `Result`, and the tests cover the new behavior.

Verification: `go test ./internal/config ./cmd/flipt` passed.