Updated `tctl auth sign --format=kubernetes` to use an HTTPS Kubernetes proxy address on port 3026. The new `ProxyConfig.KubeAddr()` method selects a Kubernetes public host when available; the command also checks registered proxies and skips invalid addresses. An explicit `--proxy` value still takes precedence.

The existing tests passed: `go test ./lib/service ./tool/tctl/common`.