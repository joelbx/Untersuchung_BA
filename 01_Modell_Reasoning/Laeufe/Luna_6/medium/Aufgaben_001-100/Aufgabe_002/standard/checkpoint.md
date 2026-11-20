# Checkpoint

Task: Fix `tctl auth sign --format=kubernetes` so generated kubeconfigs use the Kubernetes proxy address and port (3026), with a public `ProxyConfig.KubeAddr()` method.

Completed: Added `ProxyConfig.KubeAddr()` with Kubernetes public address preference, general public address fallback, HTTPS scheme, forced port 3026, and errors for disabled Kubernetes support or invalid/missing addresses. Updated kubeconfig address selection to use this method for an enabled local Kubernetes proxy, or query registered proxies and validate candidates when disabled. Explicit `--proxy` values continue to take precedence.

Verification: `go test ./lib/service ./tool/tctl/common` passed; `git diff --check` passed.
