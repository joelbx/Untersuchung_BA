# Checkpoint

Task: support `TELEPORT_KUBE_CLUSTER` in tsh configuration, preserve CLI precedence, cluster/site precedence, and TELEPORT_HOME normalization.

Status: root cause identified. `Run` parses CLI flags then calls `readClusterFlag` and `readTeleportHome`; no corresponding reader exists for `KubernetesCluster`. Existing cluster reader prefers CLI, then TELEPORT_CLUSTER, then TELEPORT_SITE. Home reader overrides CLI and calls `path.Clean`. Recent git history has one visible baseline commit and no working-tree changes.

Hypothesis: adding a Kubernetes environment reader after flag parsing, conditional on an empty CLI KubernetesCluster, will satisfy the missing behavior without changing existing precedence.

Checks: pre-fix `go test ./tool/tsh -run 'TestRead(KubeClusterFlag|ClusterFlag|TeleportHome)$' -count=1` failed to build with undefined `readKubeClusterFlag` and `kubeClusterEnvVar`, as expected. After patch, same focused command passed (exit 0). `git diff --check` passed. Full `go test ./tool/tsh -count=1` passed (exit 0, 22.610s).

Resolution: added `TELEPORT_KUBE_CLUSTER` reader after CLI parsing, using its value only when `KubernetesCluster` is empty. Added table test for empty, environment, and CLI precedence; extended home test for CLI override and slash normalization. Existing cluster/site behavior is covered by `TestReadClusterFlag` and remained unchanged.
