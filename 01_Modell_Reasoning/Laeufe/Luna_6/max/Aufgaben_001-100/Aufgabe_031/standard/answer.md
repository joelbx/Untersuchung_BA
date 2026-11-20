Updated config loading so `Load("")` applies defaults and `FLIPT_` overrides. CLI startup now uses that path when no config file is found, so environment values are honored.

Verification passed: `go test ./internal/config ./cmd/flipt` and `git diff --check`.