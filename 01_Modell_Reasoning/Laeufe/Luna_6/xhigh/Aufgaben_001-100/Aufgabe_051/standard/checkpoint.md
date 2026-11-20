# Checkpoint

Task complete: `tsh` now reads `TELEPORT_KUBE_CLUSTER` after CLI parsing and only applies it when `KubernetesCluster` was not specified on the CLI.

The existing `TELEPORT_CLUSTER`/`TELEPORT_SITE` logic already implements cluster-over-site and CLI-over-environment precedence. `TELEPORT_HOME` already overrides the CLI home and uses `path.Clean` to remove trailing slashes. Added tests cover Kubernetes selection/CLI precedence and home override/normalization/unset behavior.

Verification passed: `go test ./tool/tsh -run 'TestReadClusterFlag|TestReadKubeClusterFlag|TestReadTeleportHome'`; `git diff --check` is clean.
