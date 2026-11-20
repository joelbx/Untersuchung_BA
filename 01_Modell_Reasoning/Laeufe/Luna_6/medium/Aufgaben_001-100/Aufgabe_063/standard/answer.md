Implemented `proxy_service.kube_listen_addr` in [fileconf.go](/app/lib/config/fileconf.go) and [configuration.go](/app/lib/config/configuration.go). It enables Kubernetes proxying, parses the address with the default Kubernetes port, and takes precedence when the legacy block is explicitly disabled. Configuring it alongside an enabled legacy Kubernetes block returns a clear error. A warning is emitted when Kubernetes service and proxy are enabled but no Kubernetes listen address is set.

Existing `KubeAddr` resolution already prefers configured Kubernetes public addresses and otherwise uses the proxy’s advertised web address.

Verification: `go test ./lib/config ./lib/service` passed.