Implemented `proxy_service.kube_listen_addr`. It enables the Kubernetes proxy, uses the Kubernetes default port when none is given, and produces a clear error if the legacy Kubernetes block is also enabled. An explicitly disabled legacy block can coexist with the shorthand.

The patch also warns when the Kubernetes and proxy services are enabled without a proxy Kubernetes listen address, fixes standalone Kubernetes listener parsing, and makes clients replace wildcard listen hosts with the web proxy host while preserving the Kubernetes port. Configured Kubernetes public addresses still take priority.

The config and client test suites passed, and `git diff --check` found no whitespace errors.