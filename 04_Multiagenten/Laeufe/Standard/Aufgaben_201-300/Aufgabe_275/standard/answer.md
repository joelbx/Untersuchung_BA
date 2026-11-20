Updated Kubernetes proxy authentication so access errors remain `AccessDenied`, while cluster lookup, no-tunnel, and other non-access failures retain their trace classification. The existing no-tunnel `BadParameter` in `setupContext` is unchanged.

Added the requested `httplib` error-writer wrappers and updated the authentication test cases to check both access and non-access classifications.

Verification passed: `go test ./lib/kube/proxy ./lib/httplib` and `git diff --check`.