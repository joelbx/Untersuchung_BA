Implemented the Kubernetes proxy address fix.

- Added `ProxyConfig.KubeAddr()` to return an HTTPS address on port 3026, using the first Kubernetes public address or the generic proxy address fallback. It returns an error when Kubernetes proxy support is disabled or no usable address is configured.
- Updated kubeconfig signing to use `KubeAddr()` for a locally configured Kubernetes proxy. Otherwise, it checks registered proxies in order, skips invalid addresses, and uses the first valid host on port 3026.
- Explicit `--proxy` values remain the override.

Verification passed: `go test ./lib/service ./tool/tctl/common` and `git diff --check`.