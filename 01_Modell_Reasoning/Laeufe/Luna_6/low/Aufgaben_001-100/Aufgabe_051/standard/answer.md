Added `TELEPORT_KUBE_CLUSTER` support in `tsh`. It sets `KubernetesCluster` when no CLI value is provided; the CLI value retains precedence. Added tests for environment selection and precedence, plus `TELEPORT_HOME` override and normalization.

The existing `TELEPORT_CLUSTER`/`TELEPORT_SITE` handling already matches the requested precedence.

`gofmt` and `git diff --check` completed. The focused Go test run was interrupted while still compiling, so test results are unavailable.