# Namespace authorization fix checkpoint

Status: implementation complete; verification passed.

Changes: added `Namespaces` authorization decisions for bundle and rego engines; added the shared namespace context key and result validation; routed ListNamespaces through the namespace decision in gRPC middleware; filtered namespace results before pagination and computed a visible total; redirected the UI from inaccessible or unscoped namespace routes to an accessible namespace. Added role and malformed-result coverage.

Verification: `GOPROXY=off GOTOOLCHAIN=local go test ./internal/server/authz/... ./internal/server ./internal/cmd -count=1` passed; `git diff --check` passed. UI package dependencies are absent locally, so the UI build and Jest suite could not run without a download.

Constraints observed: local repository only; no changes to git history, index baseline, or harness configuration.
