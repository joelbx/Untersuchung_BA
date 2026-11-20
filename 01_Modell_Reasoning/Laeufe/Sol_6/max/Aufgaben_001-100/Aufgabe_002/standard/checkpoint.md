Task: Fix `tctl auth sign --format=kubernetes` so generated kubeconfigs use the Kubernetes proxy address.

Status: Complete. Implemented `ProxyConfig.KubeAddr()` with HTTPS and port 3026. `tctl auth sign` now uses it for an enabled local Kubernetes proxy and falls back to registered proxies with invalid addresses skipped. Added regression tests for local selection, registered proxy fallback, invalid addresses, and the explicit flag.

Verification: `git diff --check` and `go test ./lib/service ./tool/tctl/common -count=1` pass.
