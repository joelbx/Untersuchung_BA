# Checkpoint

Task: Restore namespace listing for users without access to default namespace.
Status: investigating root cause before edits.
Environment: `rg` is unavailable (`/bin/bash: rg: command not found`); using `grep`/`find` for local searches.
Constraints: local repository and tests only; no downloads or history/index changes.

Root cause: ListNamespaceRequest emits an unscoped read request. Middleware calls only IsAllowed, so a policy that grants reads solely for named namespaces denies listing before the service runs. The service has no context filter and reports a global count. Rego compiles only the allow query; bundle has only the allow decision path.
Pattern: authentication middleware uses a private context key and a ContextWith... helper. Namespace storage returns paged results with an independent global count. A filtered response must avoid exposing unauthorized keys or count.
Hypothesis: evaluating a dedicated viewable_namespaces policy for ListNamespaceRequest, carrying that list in context, then filtering service results resolves the 403 and disclosure.

Implemented: dedicated namespace evaluation in both OPA engines; shared result validation; middleware context propagation; filtered ListNamespaces response and authorized total count; UI navigation from inaccessible or unscoped namespace routes to an accessible namespace. Added role combinations and error/empty regression tests.

Verification: pre-fix `GOTOOLCHAIN=local GOPROXY=off go test ./internal/server/authz/middleware/grpc -run TestListNamespacesAuthorization -count=1` failed as expected: `undefined: authz.NamespacesKey`. Post-fix targeted tests passed. Final full relevant Go command is running: `GOTOOLCHAIN=local GOPROXY=off go test ./internal/server/authz/... ./internal/server -count=1`.

Offline UI check unavailable: exact command `npm --prefix ui run build` exited 127 with `/bin/bash: line 1: npm: command not found`. UI TypeScript compilation and build remain unverified; no dependencies were downloaded.
Final verification completed: `GOTOOLCHAIN=local GOPROXY=off go test ./internal/server/authz/... ./internal/server -count=1` passed (exit 0); `git diff --check` passed (exit 0).
