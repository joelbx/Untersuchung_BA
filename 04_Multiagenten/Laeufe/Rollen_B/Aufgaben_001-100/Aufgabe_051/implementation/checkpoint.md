Implementer: inspecting tsh environment defaults and tests; will verify precedence and patch.
Verified: readClusterFlag handles TELEPORT_CLUSTER/SITE precedence; readTeleportHome cleans and overrides. Kubernetes env fallback is absent. Adding reader and tests.
Patched tsh to read TELEPORT_KUBE_CLUSTER only when CLI KubernetesCluster is empty. Added precedence cases and TELEPORT_HOME override case. Focused tests running.
Focused tests passed: TestReadClusterFlag, TestReadKubeClusterFlag, TestReadTeleportHome. git diff --check passed.
