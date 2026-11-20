# Checkpoint

Resolved: `proxy_service.kube_listen_addr` enables the Kubernetes proxy, parses host:port with port 3026 as the default, and takes precedence over an explicitly disabled legacy block. Enabled legacy Kubernetes config conflicts with the shorthand and produces a clear validation error. Standalone Kubernetes plus proxy service without an explicit proxy Kubernetes listen address produces a warning. Client address resolution substitutes the web proxy host for wildcard Kubernetes listeners, preferring advertised public addresses.

Files changed: `lib/config/fileconf.go`, `lib/config/configuration.go`, `lib/config/configuration_test.go`, `lib/client/api.go`, `lib/client/api_test.go`, `docs/4.4/config-reference.md`.

Verification: `go test ./lib/config ./lib/client` passed; `git diff --check` passed. The Go C dependency emitted a compiler warning from vendored sqlite3, but tests passed. `rg` was unavailable; searches used `grep`.
