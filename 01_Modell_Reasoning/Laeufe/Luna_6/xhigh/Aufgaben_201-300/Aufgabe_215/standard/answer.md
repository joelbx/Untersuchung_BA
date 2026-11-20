Implemented HTTPS support for REST/UI and gRPC, including protocol selection, separate HTTP/HTTPS ports, TLS credential validation, and path-based configuration with `FLIPT_*` overrides. Updated the configuration examples and docs.

`go test ./cmd/flipt` and `go test ./...` passed. `git diff --check` passed.