Updated `tsh` to read `TELEPORT_KUBE_CLUSTER` when no Kubernetes cluster was specified on the CLI. The existing `TELEPORT_CLUSTER`/`TELEPORT_SITE` and `TELEPORT_HOME` precedence rules remain in place, with added test coverage for home override.

The focused `tsh` tests passed, and `git diff --check` passed.