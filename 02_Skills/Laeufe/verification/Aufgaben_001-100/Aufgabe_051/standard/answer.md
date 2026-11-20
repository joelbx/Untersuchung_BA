`tsh` now reads `TELEPORT_KUBE_CLUSTER` into `KubernetesCluster` when no Kubernetes cluster was specified on the CLI. The existing site and home environment handling remains in place; I added a test for `TELEPORT_HOME` overriding a CLI home path.

The focused `tsh` tests passed, and `git diff --check` reported no errors.