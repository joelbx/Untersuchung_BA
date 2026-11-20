Implemented the Kubernetes proxy address fix.

- Added [`ProxyConfig.KubeAddr()`](/app/lib/service/cfg.go:393), which returns an HTTPS URL on port 3026 and errors when Kubernetes proxy support is disabled or the address is invalid.
- Updated [`checkProxyAddr()`](/app/tool/tctl/common/auth_command.go:386) to honor `--proxy`, use local Kubernetes proxy configuration when enabled, or search registered proxies while skipping invalid addresses.

Verified with `go test ./lib/service ./tool/tctl/common`; both suites passed. `git diff --check` passed.