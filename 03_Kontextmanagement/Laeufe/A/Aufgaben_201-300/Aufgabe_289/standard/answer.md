Added `DefaultConfig()` and the exported `DecodeHooks` slice in [config.go](/app/internal/config/config.go). `Load` now composes those hooks, and storage’s Local and Git fields use pointers with validation for missing values. The existing default-config test now uses the exported function.

`go test ./internal/config` and `go test ./internal/cmd ./internal/config` passed.