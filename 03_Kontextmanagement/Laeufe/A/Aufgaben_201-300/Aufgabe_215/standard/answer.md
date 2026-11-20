Added HTTPS support for REST/UI and gRPC, with separate HTTP and HTTPS ports and certificate validation at startup. HTTP remains the default. Updated the configuration examples and added tests for defaults, overrides, and validation.

Verification: `go test ./...` and `git diff --check` passed.