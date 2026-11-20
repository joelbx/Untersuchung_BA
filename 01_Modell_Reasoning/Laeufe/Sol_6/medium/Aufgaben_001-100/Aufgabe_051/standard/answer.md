`tsh` now reads `TELEPORT_KUBE_CLUSTER` into `KubernetesCluster` when no Kubernetes cluster was specified on the CLI. The existing `TELEPORT_CLUSTER`/`TELEPORT_SITE` precedence and `TELEPORT_HOME` override and normalization are preserved, with added test coverage.

The focused configuration tests passed.