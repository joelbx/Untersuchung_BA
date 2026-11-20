`tsh` now reads `TELEPORT_KUBE_CLUSTER` into its CLI configuration. A cluster specified with `--kube-cluster` takes precedence. The existing `TELEPORT_CLUSTER` and `TELEPORT_SITE` precedence remains in place, and a test now covers `TELEPORT_HOME` overriding a CLI home path while removing a trailing slash.

The focused tests for all three settings passed.