Updated `authenticate` to return `AccessDenied` only when `setupContext` reports an access-denied error. Other errors are wrapped with `trace.Wrap`, preserving their classification.

Updated `TestAuthenticate` to check access-denied cases, unknown Kubernetes cluster errors, and the no-tunnel `BadParameter` case.

Validation passed: `go test ./lib/kube/proxy -count=1`.