I traced the issue but did not change project source or tests; this run was limited to fault localization.

- [fileconf.go](/app/lib/config/fileconf.go:54) rejects `kube_listen_addr` as an unknown key, and `Proxy` has no field for it.
- [configuration.go](/app/lib/config/configuration.go:542) enables the Kubernetes proxy only through the nested block. This is the likely place to parse the shorthand with the existing Kubernetes default port (3026), reject it when the nested block is enabled, accept it when that block is explicitly disabled, and warn when both services are enabled without a proxy Kubernetes listener.
- [api.go](/app/lib/client/api.go:1907) already prefers a Kubernetes public address, but passes a wildcard listen host (`0.0.0.0` or `::`) to clients unchanged. It should use the web proxy host while retaining the Kubernetes port.

The existing config test I found checks only that the Kubernetes proxy is disabled by default. An adjacent, unverified issue is that [applyKubeConfig](/app/lib/config/configuration.go:655) reads the proxy SSH listen address when setting the standalone Kubernetes listener.