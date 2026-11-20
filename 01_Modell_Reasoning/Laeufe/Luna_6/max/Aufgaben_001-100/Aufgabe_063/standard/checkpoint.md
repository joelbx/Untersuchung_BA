# Checkpoint

Task: implement `proxy_service.kube_listen_addr` shorthand, validation and precedence, missing-address warning, and client handling of wildcard Kubernetes proxy hosts.

Implemented:
- Added the top-level proxy config field and recognized it during YAML key validation.
- Added a clear configuration error when the shorthand conflicts with explicitly enabled legacy `proxy_service.kubernetes` settings.
- Applied shorthand address parsing with the Kubernetes default port, enabling the proxy and overriding the nested listen address, including when the nested block is explicitly disabled.
- Added a warning for an enabled Kubernetes service when its enabled proxy has no explicit Kubernetes listen address.
- Updated client resolution to replace wildcard Kubernetes hosts (`0.0.0.0` and `::`) with the web proxy host while retaining configured public-address precedence.

Verification: `go test ./lib/config ./lib/client` passed. `git diff --check` passed. `rg` is unavailable; repository searches used `grep` and `find`.
