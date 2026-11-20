Implemented `proxy_service.kube_listen_addr` shorthand with Kubernetes proxy activation, the default Kubernetes port, and validation that rejects combining it with an enabled legacy Kubernetes block. An explicitly disabled legacy block can coexist with the shorthand, which takes precedence.

Also added a warning when the standalone Kubernetes service and proxy are both enabled without a proxy Kubernetes listen address. Client address resolution now substitutes the web proxy host when the Kubernetes address uses an unspecified or loopback host. Configured public Kubernetes addresses retain priority.

Added shorthand parsing and conflict tests. `go test ./lib/config ./lib/client` passes; `git diff --check` is clean. The build emitted a warning from the existing SQLite C source.