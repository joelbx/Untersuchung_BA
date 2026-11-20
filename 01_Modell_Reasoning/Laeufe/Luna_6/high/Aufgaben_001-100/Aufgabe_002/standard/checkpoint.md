# Checkpoint

Implemented the Kubernetes proxy address fix.

- Added `service.ProxyConfig.KubeAddr()` to require Kubernetes proxy support, use the first Kubernetes public address (or generic proxy public address fallback), replace its port with 3026, and return an HTTPS URL.
- Updated `tctl auth sign --format=kubernetes` address selection to use `KubeAddr()` for a local Kubernetes-enabled proxy. Otherwise it checks registered proxies in order, skips invalid addresses, and selects the first valid host on port 3026.
- Kept explicit `--proxy` values as the direct override.

Verification: `go test ./lib/service ./tool/tctl/common` passed. `git diff --check` passed.
