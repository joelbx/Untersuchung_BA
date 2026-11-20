# Checkpoint

Task: Fix namespace authorization so users without access to the default namespace can load the UI and see only namespaces they can access.

Completed:
- Added `Verifier.Namespaces`, typed result validation, and context helpers using `NamespacesKey`.
- Implemented bundle and local Rego evaluation for `viewable_namespaces` decisions, including undefined and malformed result errors.
- Routed ListNamespaces through the dedicated decision and filtered results/count in the server method.
- Added role mapping, middleware, engine, and service tests.

Verification:
- `go test ./internal/server/authz/... ./internal/server -run 'Test(Engine|AuthorizationRequiredInterceptor|ListNamespaces)'`
- `go test ./internal/cmd -run '^$'`
- `git diff --check`
