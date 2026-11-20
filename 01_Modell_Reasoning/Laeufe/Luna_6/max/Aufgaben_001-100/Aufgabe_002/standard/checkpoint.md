# Checkpoint

Task completed: `tctl auth sign --format=kubernetes` now resolves a Kubernetes proxy address on port 3026.

Implementation:
- Added `ProxyConfig.KubeAddr()` with disabled and missing/invalid address errors, selection of the first Kubernetes public address or proxy public address, HTTPS scheme, and the default Kubernetes port.
- Updated tctl to honor explicit `--proxy`, use `KubeAddr()` when local Kubernetes proxy support is enabled, and otherwise scan registered proxies while skipping invalid public addresses.

Verification: `go test ./lib/service ./tool/tctl/common` passed after the final changes. `git diff --check` passed.
