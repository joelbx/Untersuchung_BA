Task: Support TELEPORT_KUBE_CLUSTER in tsh configuration and verify environment precedence.
Status: complete.
Changes: tsh Run reads TELEPORT_KUBE_CLUSTER after parsing; CLI KubernetesCluster takes precedence. Added focused tests for unset, environment, and CLI cases. Existing cluster precedence tests pass; home test now checks environment override and trailing-slash normalization.
Verification: go test ./tool/tsh -run '^(TestReadClusterFlag|TestReadKubeClusterFlag|TestReadTeleportHome)$' -count=1 (passed); git diff --check (passed).
