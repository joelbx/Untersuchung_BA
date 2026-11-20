# Checkpoint

Task: Resolve namespace listing authorization so users without `default` access can load the UI, and expose only authorized namespaces.

Implemented:
- Added namespace evaluation to the shared authorization interface and both OPA engines. Bundle evaluates `flipt/authz/v1/viewable_namespaces`; local Rego evaluates `data.flipt.authz.v1.viewable_namespaces`.
- Added validation for undefined and malformed namespace decision results.
- The gRPC interceptor recognizes `ListNamespaceRequest`, evaluates viewable namespaces for the authenticated user, stores them in context, and bypasses the default-namespace list authorization check.
- The namespace service filters before pagination and reports the accessible namespace count.

Verification: `go test ./internal/server/authz/... ./internal/server -run 'Test(AuthorizationRequiredInterceptor|ListNamespaces|Engine_)'` passed. `git diff --check` passed.

Notes: Role-to-namespace mappings are policy-defined; the engines pass the authenticated identity to the required decision path and return the policy's namespace list. A policy with no `viewable_namespaces` decision returns an error.
