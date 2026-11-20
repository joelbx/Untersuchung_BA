Implemented HTTPS support in `/app`: protocol and port configuration, certificate validation, TLS for REST/UI and gRPC, and a secure internal gateway connection. Updated the configuration examples and documentation, and added tests.

`GOPROXY=off go test ./...` and `git diff --check` pass.