Implemented and registered `flipt.is_auth_method(input, method)` for the local Rego engine. It maps the supported labels to protobuf enum values, including the `k8s` alias, and returns the required errors for missing authentication and unsupported labels.

Added coverage in [extentions_test.go](/app/internal/server/authz/engine/ext/extentions_test.go:1); registration is implemented in [extentions.go](/app/internal/server/authz/engine/ext/extentions.go:13).

**Verification:** `go test ./internal/server/authz/...` passed.