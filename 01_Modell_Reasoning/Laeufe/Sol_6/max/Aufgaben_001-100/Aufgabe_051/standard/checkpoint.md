Task: Add TELEPORT_KUBE_CLUSTER support to tsh CLI configuration, preserve CLI precedence, and verify related environment variables.

Status: Implemented and verified. `Run` applies TELEPORT_KUBE_CLUSTER after CLI parsing, while preserving any selected Kubernetes cluster. Updated CLI reference and tests for Kubernetes cluster precedence and TELEPORT_HOME override.

Verification: `go test -mod=vendor ./tool/tsh -run 'Test(ReadClusterFlag|ReadKubeClusterFlag|ReadTeleportHome|KubeConfigUpdate)$' -count=1` passed.
