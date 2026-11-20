Implemented namespace authorization through a dedicated `viewable_namespaces` decision in both engines. The middleware now uses that decision for ListNamespaces requests, and the endpoint filters results and reports the accessible namespace count. Added role mapping, context, filtering, and malformed-result coverage.

Verified with:

- `go test ./internal/server/authz/... ./internal/server -run 'Test(Engine|AuthorizationRequiredInterceptor|ListNamespaces)'`
- `go test ./internal/cmd -run '^$'`
- `git diff --check`