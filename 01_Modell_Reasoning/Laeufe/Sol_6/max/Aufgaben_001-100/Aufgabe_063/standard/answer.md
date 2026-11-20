Implemented `proxy_service.kube_listen_addr` as a shorthand that enables the Kubernetes proxy. Configuration now rejects conflicts with an enabled legacy Kubernetes block, accepts an explicitly disabled block with the shorthand taking precedence, and preserves legacy configuration. It also warns when an enabled Kubernetes service has no proxy Kubernetes listen address.

Client address resolution now replaces wildcard listen hosts with the web proxy host while retaining the Kubernetes port and preferring configured public addresses. I updated the [configuration reference](/app/docs/4.4/config-reference.md) and added regression coverage.

Validation passed: `go test -mod=vendor ./lib/config ./lib/client` and `git diff --check`.