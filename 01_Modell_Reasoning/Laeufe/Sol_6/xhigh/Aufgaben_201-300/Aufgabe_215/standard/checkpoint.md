# HTTPS support checkpoint

Task: add configurable HTTPS for REST/UI and gRPC, validate TLS credentials, preserve HTTP defaults, and verify with existing tests.

Status: implementation complete. Configuration now supports HTTP/HTTPS, distinct ports, certificate paths, validation, and environment overrides. Both REST/UI and gRPC serve TLS when HTTPS is selected; the REST gateway pins the configured certificate for its local gRPC connection. Documentation and focused configuration tests were added.

Verification: `GOPROXY=off GOSUMDB=off go test ./...` passed. Local HTTPS smoke test returned HTTP 200 from `/meta/info` and `/api/v1/flags`; `openssl s_client` verified the gRPC TLS certificate.
