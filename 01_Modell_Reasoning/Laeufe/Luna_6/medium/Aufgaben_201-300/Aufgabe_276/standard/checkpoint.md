# Checkpoint

Implemented startup validation for enabled GitHub and configured OIDC providers. Required credential and redirect fields reject empty or whitespace-only values with provider and field names. GitHub organization restrictions require `read:org` with the specified error format. Updated the existing config test expectation for that message.

Verification: `go test ./internal/config` passes.
