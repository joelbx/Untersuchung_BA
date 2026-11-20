# Checkpoint

Task: add configurable HTTPS support and satisfy the configuration/handler requirements in the repository issue.

Implemented:
- Added `Scheme` (`HTTP`/`HTTPS`) and string JSON representation.
- Reworked `configure(path)` to use an isolated Viper instance, defaults sourced from `defaultConfig()`, YAML values, and `FLIPT_*` environment overrides; all required keys are mapped and validation errors are returned directly.
- Added HTTPS credential presence, file existence, and key-pair validation.
- Routed REST/UI through the selected protocol and its corresponding port; configured TLS for the gRPC listener and gateway client.
- Preserved CORS scalar strings as one origin, and updated config examples and documentation.

Verification: `go test ./...` passed; `git diff --check` passed. The test run emitted the existing sqlite3 C compiler warning about returning the address of a local variable. No tests exist in `cmd/flipt`.
