# Kubernetes proxy shorthand work

- Task: add `proxy_service.kube_listen_addr` shorthand while preserving legacy Kubernetes configuration.
- Added YAML acceptance, conflict validation, shorthand precedence, and the missing-listen warning.
- Corrected standalone Kubernetes service listen address parsing and client wildcard host resolution, including IPv6 URL formatting.
- Added focused configuration and client tests. `go test ./lib/config ./lib/client ./lib/service` passed; `git diff --check` passed.
