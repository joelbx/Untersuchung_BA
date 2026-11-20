# Checkpoint

Task: fix Kubernetes proxy address selection in `tctl auth sign --format=kubernetes`.

Completed: added `ProxyConfig.KubeAddr()` to build an HTTPS URL on port 3026 from the Kubernetes public host, falling back to the web public host. Updated signing to use the local Kubernetes proxy when enabled, otherwise to search registered proxies and skip invalid public addresses. Added regression coverage for helper behavior, proxy fallback, and generated kubeconfig server URL.

Verification: `go test ./lib/service ./tool/tctl/common -count=1` passed; `git diff --check` passed.
