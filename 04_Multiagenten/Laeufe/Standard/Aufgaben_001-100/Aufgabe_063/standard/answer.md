Implemented `proxy_service.kube_listen_addr` in the checked-out repository. It enables the Kubernetes proxy, uses the Kubernetes default port when needed, and takes precedence over an explicitly disabled legacy block. An enabled legacy block combined with the shorthand now produces a clear conflict error.

The configuration warns when both Kubernetes and proxy services are enabled without an explicit Kubernetes proxy listen address. Client resolution replaces `0.0.0.0` or `::` with the web proxy host and continues to prefer configured public addresses.

Added focused configuration and client tests. `go test ./lib/config ./lib/client` and `git diff --check` pass.