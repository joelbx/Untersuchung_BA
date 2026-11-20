Implemented configurable HTTP/HTTPS serving, separate HTTP and HTTPS ports, certificate validation, YAML and environment overrides, and TLS for REST/UI and gRPC. Updated startup to load config from the provided path.

Verification: `go test ./cmd/flipt` passed, and `git diff --check` passed. The package has no test files.