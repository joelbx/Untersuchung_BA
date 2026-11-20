Implemented `proxy_service.kube_listen_addr` with Kubernetes port defaults, proxy enablement, shorthand precedence over an explicitly disabled legacy block, and a clear error when both settings are enabled. Added the missing-listen-address warning and client resolution for wildcard Kubernetes hosts, while preserving public-address priority.

Relevant changes are in [fileconf.go](/app/lib/config/fileconf.go:341), [configuration.go](/app/lib/config/configuration.go:541), and [api.go](/app/lib/client/api.go:689).

Verification passed: `go test ./lib/config ./lib/client`.