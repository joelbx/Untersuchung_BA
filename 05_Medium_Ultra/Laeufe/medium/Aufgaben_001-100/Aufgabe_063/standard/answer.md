Implemented `proxy_service.kube_listen_addr` as a shorthand that enables the Kubernetes proxy and uses the Kubernetes default port when no port is given. Configuration now rejects an enabled legacy Kubernetes block alongside the shorthand, accepts an explicitly disabled block with the shorthand, and warns when both Kubernetes and proxy services are enabled without a proxy Kubernetes listen address.

Client address resolution now uses the web proxy host for unspecified listen hosts (`0.0.0.0` and `::`) and gives configured Kubernetes public addresses priority. Existing legacy configuration remains supported.

Verification passed: `go test ./lib/config ./lib/client` and `git diff --check`.