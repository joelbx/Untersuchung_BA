Implemented the namespace access fix in [/app](/app).

The bundle and rego engines now evaluate `viewable_namespaces` and reject undefined or malformed results. The middleware passes the accessible namespace list to [ListNamespaces](/app/internal/server/namespace.go), which filters before pagination and reports the accessible total. The UI redirects from an inaccessible namespace to one the user can access and shows only returned namespaces in the dropdown.

Engine, middleware, and UI changes were delegated to subagents; I integrated and reviewed the patch. Server and authorization tests pass, as does the `internal/cmd` compile check and `git diff --check`. UI tests and typecheck could not run because Node, npm, and UI dependencies are absent.