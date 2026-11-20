# Checkpoint

Implemented startup-time validation for GitHub and each configured OIDC provider when their authentication method is enabled. Required OAuth fields reject empty or whitespace-only values with provider and field context. GitHub's organization scope error now includes the required provider and field context. Added configuration loading coverage and updated the existing scope fixture. `go test ./internal/config` passes; `git diff --check` passes.
