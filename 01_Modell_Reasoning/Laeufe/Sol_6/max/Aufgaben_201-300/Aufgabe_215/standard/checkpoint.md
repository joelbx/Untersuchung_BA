# HTTPS support checkpoint

- Implemented `Scheme`, path-based YAML loading with `FLIPT_` environment overrides, server protocol/port/certificate settings, stable defaults, and exact HTTPS path validation errors.
- HTTPS serves REST/UI and gRPC with the configured key pair. The REST gateway verifies its TLS connection to gRPC. HTTP remains the default.
- Added configuration tests, advanced/default YAML fixtures, a test-only self-signed certificate/key, and configuration documentation. Narrowed `.gitignore` so new `cmd/flipt` files are visible to the coordinator.
- Verification: `go test ./... -count=1` passed; `git diff --check` passed. Live HTTP and HTTPS smoke checks returned 200 for metadata and REST gateway; the HTTPS gRPC port negotiated TLS with HTTP/2.
- Remaining work: none.
