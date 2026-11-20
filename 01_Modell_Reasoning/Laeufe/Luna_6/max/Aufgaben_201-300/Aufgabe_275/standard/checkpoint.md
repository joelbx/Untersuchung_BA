# Checkpoint

Task: Fix Kubernetes proxy `authenticate` error classification while preserving the existing `setupContext` classifications.

Findings: `setupContext` returns `BadParameter` for an unregistered local Kubernetes cluster and for a remote cluster when no reverse tunnel is configured. It may also return `AccessDenied` for remote user access to another remote cluster. `authenticate` was replacing every one of these with a generic `AccessDenied`.

Changes: `authenticate` now maps only an `AccessDenied` from `setupContext` to its generic access-denied response and wraps all other errors. `TestAuthenticate` checks classifications for authorization failure, unsupported users, unknown clusters, and missing reverse tunnels.

Verification: `go test ./lib/kube/proxy` passed. `git diff --check` passed. Go emitted a warning in vendored SQLite C code during compilation.
