Implemented `proxy_service.kube_listen_addr` as a shorthand that enables the Kubernetes proxy. Config validation rejects it alongside an explicitly enabled legacy Kubernetes block, while an explicitly disabled legacy block allows the shorthand to take precedence.

The change also adds the missing listen address warning, corrects standalone Kubernetes service address parsing, and resolves wildcard Kubernetes listen hosts through the web proxy address. Configured public addresses retain priority.

`go test ./lib/config ./lib/client ./lib/service` and `git diff --check` passed.