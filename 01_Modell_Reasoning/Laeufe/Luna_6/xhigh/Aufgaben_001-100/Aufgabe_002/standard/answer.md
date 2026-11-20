Implemented Kubernetes proxy address selection.

- Added [ProxyConfig.KubeAddr](</app/lib/service/cfg.go:393>), which returns an HTTPS URL on port 3026 and errors when Kubernetes proxy support is disabled or the address is invalid.
- Updated [tctl auth sign address selection](</app/tool/tctl/common/auth_command.go:386>) to use that method for an enabled local proxy, or search registered proxies and skip invalid addresses. An explicit `--proxy` remains in effect.

Verification passed: `go test ./lib/service ./tool/tctl/common` and `git diff --check`.