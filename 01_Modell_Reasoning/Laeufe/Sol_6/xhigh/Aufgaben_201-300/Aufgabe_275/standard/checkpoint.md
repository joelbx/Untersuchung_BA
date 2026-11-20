# Checkpoint

- Issue: Kubernetes proxy `authenticate` reclassifies every `setupContext` error as `AccessDenied`.
- Found the conversion in `lib/kube/proxy/forwarder.go`; `setupContext` already returns trace-classified errors, including `BadParameter` when no reverse tunnel is available.
- `authenticate` now wraps non-access errors from authorization and `setupContext`, preserving their trace classification.
- `TestAuthenticate` checks access denials, non-access `BadParameter` errors, and original error messages.
- Added the requested `httplib` error-writer wrappers while keeping the existing handlers' default behavior.
- Verification passed: `go test ./lib/kube/proxy -run '^TestAuthenticate$' -count=1`, `go test ./lib/kube/proxy -count=1`, and `go test ./lib/httplib -count=1`.
