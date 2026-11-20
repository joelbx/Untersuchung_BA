# Checkpoint

Resolved Kubernetes kubeconfig proxy address selection.

- Added `ProxyConfig.KubeAddr()` to return an HTTPS URL on Kubernetes proxy port 3026, preferring Kubernetes public addresses and skipping malformed entries.
- Updated `tctl auth sign --format=kubernetes` to use the local Kubernetes proxy when enabled, otherwise search registered proxies, skipping invalid addresses. Explicit `--proxy` remains the override.
- Added regression coverage for local, registered, malformed, IPv6, and explicit addresses.
- Verified with `go test ./lib/service ./tool/tctl/common` and `git diff --check`.
