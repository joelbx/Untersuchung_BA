# Checkpoint

Task: Fix Kubernetes proxy address selection for `tctl auth sign --format=kubernetes` in `/app`.

Constraints: Use local repository code and existing tests only. Do not access credentials, private process files, benchmark solutions, evaluator artifacts, or request downloads. Preserve git history, index baseline, and harness configuration.

Completed:
- Added `ProxyConfig.KubeAddr()`, requiring Kubernetes proxy support and returning an HTTPS URL on port 3026 from the first Kubernetes public address, or the first general proxy public address as fallback.
- Updated `tctl auth sign` address selection to honor an explicit `--proxy`, use local `KubeAddr()` when enabled, and otherwise query registered proxies while skipping invalid public addresses.
- Formatted changes and verified `git diff --check`.
- Existing tests pass: `go test ./lib/service ./tool/tctl/common`.

Working tree changes are limited to `lib/service/cfg.go` and `tool/tctl/common/auth_command.go` (the checkpoint file is ignored by git).
