Added `proxy_service.kube_listen_addr` as a shorthand that enables the Kubernetes proxy and uses the Kubernetes default port when none is given. An enabled legacy Kubernetes block now produces a clear conflict error; an explicitly disabled block allows the shorthand to take precedence.

Clients now replace unspecified Kubernetes listen hosts with the web proxy host while preferring a configured Kubernetes public address. The proxy also warns when an explicitly enabled standalone Kubernetes service has no proxy Kubernetes listen address.

The existing legacy format remains supported. `go test ./lib/config ./lib/client` and `git diff --check` passed.