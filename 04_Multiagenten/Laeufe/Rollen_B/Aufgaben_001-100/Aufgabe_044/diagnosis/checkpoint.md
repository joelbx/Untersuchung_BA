Progress: fault localization complete from local code and existing tests.
- rpc/flipt/request.go:106 emits namespace read with empty namespace for ListNamespaceRequest.
- internal/server/authz/middleware/grpc/middleware.go:85-119 sends every Request through IsAllowed; there is no ListNamespaces special case or context propagation.
- internal/server/authz/authz.go and both engine files expose only IsAllowed; bundle targets flipt/authz/v1/allow, rego prepares data.flipt.authz.v1.allow. No Namespaces method, NamespacesKey, or viewable_namespaces query exists.
- internal/server/namespace.go:22-45 returns all listed namespaces and global CountNamespaces; existing tests cover pagination only, not authorization filtering.
- ui/src/app/namespaces/namespacesSlice.ts selects first available namespace when default absent, but ui/src/app/Layout.tsx depends on successful list query. Need verify redirect semantics if implementation extends UI.
- Behavior to cover: empty authorized list, devs -> local/staging, ops -> production, combined union, missing/malformed policy decision, authorized count and pagination, absent context when authz disabled.
