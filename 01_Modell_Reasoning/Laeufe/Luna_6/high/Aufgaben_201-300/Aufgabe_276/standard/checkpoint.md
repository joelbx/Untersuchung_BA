# Checkpoint

Implemented startup validation for enabled GitHub and OIDC authentication methods. Required credentials and redirect addresses reject empty or whitespace-only values with provider-qualified errors; GitHub organization restrictions require `read:org` with the specified error format. Provider checks run before session-domain checks so these configuration errors are surfaced directly.

Added coverage for every required field and GitHub organization scope validation. Updated the existing YAML fixture so it reaches the scope check with valid GitHub credentials.

Verification: `go test ./internal/config` passed.
