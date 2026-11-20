Implemented `flipt.is_auth_method` with exactly two arguments, protocol enum mappings for all seven supported names, and the `k8s` alias. The Rego engine now loads the extension, which handles numeric and protobuf enum string inputs and returns the requested errors.

Added coverage for matches, mismatches, aliases, errors, and engine integration.

**Verification:** `go test ./internal/server/authz/...` passed.

Files: [extentions.go](/app/internal/server/authz/engine/ext/extentions.go:1), [engine.go](/app/internal/server/authz/engine/rego/engine.go:16), [engine_test.go](/app/internal/server/authz/engine/rego/engine_test.go:29).