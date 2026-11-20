# Namespace authorization fix

Implemented namespace decisions in bundle and rego engines, middleware context propagation, filtered namespace listing and count, and UI redirect from inaccessible namespace routes. Added focused role, error, middleware, and service tests.

Verification: `go test ./internal/server/authz/... ./internal/server -count=1` passed. UI dependencies are absent locally, so its build and Jest checks could not run without downloads.
