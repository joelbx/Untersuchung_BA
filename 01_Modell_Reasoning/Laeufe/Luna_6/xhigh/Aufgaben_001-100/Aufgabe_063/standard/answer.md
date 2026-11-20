Implemented `proxy_service.kube_listen_addr` shorthand with Kubernetes default port handling, enablement, conflict validation, and precedence over an explicitly disabled legacy block. Added a warning for enabled standalone Kubernetes services when the proxy has no Kubernetes listener address.

Client address resolution now replaces `0.0.0.0` and `::` listener hosts with the web proxy host, while preserving Kubernetes public address priority.

Verification passed: `go test ./lib/config ./lib/client` and `git diff --check`. Updates are in [fileconf.go](/app/lib/config/fileconf.go), [configuration.go](/app/lib/config/configuration.go), and [api.go](/app/lib/client/api.go).