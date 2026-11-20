Updated `authenticate` to wrap and preserve `setupContext` errors, keeping `BadParameter` and not-found errors non-access-denied. The existing tests now check those classifications while retaining access-denied checks for authorization failures and unsupported user types.

`go test ./lib/kube/proxy` and `git diff --check` passed.