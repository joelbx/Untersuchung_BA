VERDICT: FIX

**Code defect:** The API patch filters the namespace list, but the UI does not redirect an unauthorized namespace route. [Layout.tsx](/app/ui/src/app/Layout.tsx:43) leaves `/namespaces/default/...` in place after the list loads, while [namespacesSlice.ts](/app/ui/src/app/namespaces/namespacesSlice.ts:21) initializes the selection to `default`. A user with access only to `local` can therefore still reach pages that request `default` and receive 403 errors. After loading the list, select an accessible namespace and replace an unauthorized route, while preserving valid deep links.

**Tests:** `go test ./internal/server/authz/... ./internal/server -run 'Test(Engine_Namespaces|Engine_IsAllowed|AuthorizationRequiredInterceptor|FormatNamespaces|ListNamespaces)' -count=1` exited 0. The relevant authz, bundle, rego, middleware, and server tests passed.

**TEST_ENVIRONMENT_PROBLEM:** None.