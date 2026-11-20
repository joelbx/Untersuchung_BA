# Checkpoint

- Task: add `TELEPORT_KUBE_CLUSTER` handling and verify environment/CLI precedence for Kubernetes cluster, site, and home in `tsh`.
- Repository: `/app`; initial worktree status clean.
- `rg` is unavailable (`/bin/bash: rg: command not found`); using local `grep`/`find`.
- Next: inspect CLI configuration code and tests, patch, run relevant tests.
- Found existing `readClusterFlag` and `readTeleportHome` behavior matching requested site/home precedence. Added `readKubeClusterFlag` to `Run` after CLI parsing; added Kubernetes cluster precedence and home override cases to `tsh` tests.
- `gofmt` and `git diff --check` completed (exit 0).
- `go test ./tool/tsh -run 'TestRead(ClusterFlag|KubeClusterFlag|TeleportHome)$' -count=1` passed (exit 0; `ok github.com/gravitational/teleport/tool/tsh 0.048s`).
