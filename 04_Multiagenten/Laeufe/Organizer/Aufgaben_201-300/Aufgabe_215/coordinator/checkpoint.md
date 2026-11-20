# Checkpoint

Task: add HTTPS configuration and serving support while preserving HTTP defaults.
Completed: isolated path-based Viper loading with FLIPT environment overrides, Scheme and server defaults, exact TLS prerequisite errors, HTTPS REST/UI and TLS gRPC serving, TLS gateway dialing, configuration docs and test certificate fixture.
Verification: go test ./... passed; git diff --check passed. The legacy sqlite3 C warning is emitted during tests.
Delegation: none.
