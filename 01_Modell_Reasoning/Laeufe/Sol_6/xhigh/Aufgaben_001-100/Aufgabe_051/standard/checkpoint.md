# Checkpoint

Task: support `TELEPORT_KUBE_CLUSTER` in `tsh` while preserving CLI precedence and existing cluster/home environment behavior.

Implemented:
- Read `TELEPORT_KUBE_CLUSTER` into `CLIConf.KubernetesCluster` after CLI parsing when no CLI Kubernetes cluster was selected.
- Updated the kubeconfig selection comment to reflect environment selection.
- Added Kubernetes cluster precedence cases and home override coverage to existing `tsh` tests.

Verification:
- `GOPROXY=off GOSUMDB=off go test -mod=vendor ./tool/tsh -run 'Test(ReadClusterFlag|ReadKubeClusterFlag|ReadTeleportHome|KubeConfigUpdate)$' -count=1` passed.
- `git diff --check` passed.
