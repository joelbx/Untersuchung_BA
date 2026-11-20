Implemented namespace access evaluation in both authorization engines, special handling for `ListNamespaces` in the gRPC middleware, and context-based namespace filtering in the endpoint.

Added Rego engine coverage and a namespace filtering test. Verification passed: `go test ./internal/server/authz/... ./internal/server` and `git diff --check`.

One limitation: `TotalCount` for filtered results is calculated from the current page after filtering, so it may not reflect all accessible namespaces when pagination is used.