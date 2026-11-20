`tsh` now recognizes `TELEPORT_KUBE_CLUSTER` and uses it when no Kubernetes cluster was specified on the CLI. The existing `TELEPORT_CLUSTER`/`TELEPORT_SITE` and `TELEPORT_HOME` precedence rules remain in place; I added test coverage for the home override.

The focused `tsh` tests pass.