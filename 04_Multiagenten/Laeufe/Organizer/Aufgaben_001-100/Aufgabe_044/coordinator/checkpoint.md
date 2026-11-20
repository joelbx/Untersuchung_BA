Task: Fix namespace listing under strict authorization.
Status: implementation and focused tests complete.
Changes: namespace policy evaluation in both engines; typed context key; middleware passes visible namespaces; ListNamespaces filters before pagination and returns visible count; tests cover roles, errors, middleware, and pagination.
Verification: go test ./internal/server/authz/... ./internal/server -count=1 (passed); git diff --check passed..
Delegation: none.
