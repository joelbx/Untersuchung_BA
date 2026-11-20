Implemented HTTPS support with `server.protocol`, separate HTTP/HTTPS ports, certificate paths, and TLS listeners for the API, UI, and gRPC. Configuration now loads from the supplied YAML path, applies `FLIPT_*` overrides over defaults, and validates HTTPS certificate paths.

Updated the sample configuration and [configuration docs](/app/docs/configuration.md).

Verification: `go test ./...` passed. The sqlite3 dependency emitted a compiler warning about a possible local address return.