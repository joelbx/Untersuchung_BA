# Checkpoint

Task: add TELEPORT_KUBE_CLUSTER handling and verify environment/CLI precedence in tsh.

Plan: locate configuration assembly, add failing regression tests, implement minimal fix, run targeted and repository tests.

Tooling: `rg` is unavailable (`/bin/bash: rg: command not found`); using grep/find.

Red: `GOPROXY=off go test -mod=vendor ./tool/tsh -run 'TestReadKubeClusterFromEnvironment|TestReadClusterFlag|TestReadTeleportHome' -count=1` failed because KubernetesCluster stayed empty with TELEPORT_KUBE_CLUSTER set. A second red run also verified a CLI SiteName did not mask the missing Kubernetes default.

Green: the same targeted command passed after adding the environment default. `GOPROXY=off go test -mod=vendor ./tool/tsh -count=1` passed.

Repository-wide `GOPROXY=off go test -mod=vendor ./...` was started, then interrupted after approximately five minutes while an integration test was still active. It printed four `[no test files]` package results and no failure messages before interruption; exit code was 1 from Ctrl-C. The remaining packages are unverified by that run.
