Task: enforce required GitHub and OIDC authentication configuration fields at startup, including GitHub read:org scope and exact provider-key errors.
Status: complete. Required fields and scope validated at Load; YAML OIDC provider spelling preserved; fixture and startup tests updated. go test ./internal/config and go test ./internal/server/auth/... pass; git diff --check passes.
Constraints: local repository only; git history, index baseline, and harness configuration untouched.
