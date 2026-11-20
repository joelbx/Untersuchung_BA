# Work checkpoint

Issue: add `proxy_service.kube_listen_addr` shorthand for Kubernetes proxy listening configuration, with compatibility/conflict rules and address resolution behavior.

Implemented:
- Added the proxy YAML field and key validation; shorthand parses using the Kubernetes default port and enables the proxy.
- Rejects shorthand with an explicitly enabled legacy Kubernetes proxy block. An explicitly disabled legacy block can be overridden by the shorthand.
- Warns when an explicitly enabled standalone Kubernetes service and the proxy are both enabled but no Kubernetes listener address is configured on the proxy.
- Client resolution replaces wildcard Kubernetes listener hosts with the advertised web proxy host (or configured web proxy host), while keeping configured Kubernetes public addresses first.
- Added focused config and client tests, including legacy compatibility.

Verification: `go test ./lib/config ./lib/client` passed. `git diff --check` passed.
