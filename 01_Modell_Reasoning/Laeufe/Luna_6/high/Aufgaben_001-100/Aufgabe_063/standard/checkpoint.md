# Checkpoint

Task: implement the `proxy_service.kube_listen_addr` shorthand for Kubernetes proxy configuration.

Implemented:
- Added the YAML field and accepted key.
- The shorthand parses host/port with the Kubernetes default port and enables the proxy.
- Explicitly enabled legacy `proxy_service.kubernetes` plus shorthand returns a clear configuration error; an explicitly disabled legacy block can be overridden by the shorthand.
- Added a warning when an explicitly enabled Kubernetes service has no Kubernetes proxy listen address.
- Client resolution replaces wildcard IPv4/IPv6 listen hosts with the web proxy hostname. Existing configured public address precedence remains intact.

Verification: `go test ./lib/config ./lib/client` passed. `git diff --check` passed.
