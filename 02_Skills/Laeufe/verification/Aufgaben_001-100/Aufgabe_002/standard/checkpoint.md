# Checkpoint

- Task: fix Kubernetes proxy address selection in `tctl auth sign --format=kubernetes`.
- Initial search: `rg` is unavailable (`/bin/bash: rg: command not found`); using `grep`/`find` locally.
- Added `ProxyConfig.KubeAddr()` and updated `tctl auth sign` address selection. Malformed public addresses are skipped.
- Added service address tests and command tests, including generated kubeconfig server address.
- Verification: `go test ./lib/service ./tool/tctl/common` exited 0 (`lib/service` and `tool/tctl/common` both `ok`). `git diff --check` exited 0. The Go build emitted a warning in vendored `go-sqlite3`, without a test failure.
