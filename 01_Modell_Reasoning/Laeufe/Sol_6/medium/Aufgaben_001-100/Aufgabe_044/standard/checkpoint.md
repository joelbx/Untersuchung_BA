# Namespace authorization fix

Completed: bundle and rego namespace decisions, validated namespace result formatting, middleware context handoff, filtered namespace listing and visible total count, and UI redirect to an authorized namespace. Added role mapping, malformed-result, middleware, context, and service tests.

Verification: `go test ./internal/server/authz/... ./internal/server -count=1` passed; `git diff --check` passed. UI tests could not run because `ui/node_modules` is absent and downloads are disallowed.
