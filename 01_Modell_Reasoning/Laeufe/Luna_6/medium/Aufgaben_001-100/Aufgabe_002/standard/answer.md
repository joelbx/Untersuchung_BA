Implemented Kubernetes proxy address selection in [cfg.go](/app/lib/service/cfg.go) and [auth_command.go](/app/tool/tctl/common/auth_command.go). Kubeconfigs now use HTTPS on port 3026, preferring Kubernetes public addresses and skipping invalid registered proxy addresses. An explicit `--proxy` value remains the override.

`go test ./lib/service ./tool/tctl/common` and `git diff --check` passed.