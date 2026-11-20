Implemented `flipt.is_auth_method(input, method)` and registered it with the Rego engine. Supported names map to protobuf enum constants, including `k8s` and `kubernetes` as aliases. Missing authentication and unsupported names return the requested errors.

Added coverage for supported methods, mismatches, aliases, and errors in [extentions_test.go](/app/internal/server/authz/engine/ext/extentions_test.go).

Verification passed: `go test ./internal/server/authz/engine/ext ./internal/server/authz/engine/rego`.