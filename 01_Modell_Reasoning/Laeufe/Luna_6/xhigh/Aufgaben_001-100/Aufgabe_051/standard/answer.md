Added `TELEPORT_KUBE_CLUSTER` support in [tsh.go](/app/tool/tsh/tsh.go:275). It sets `KubernetesCluster` only when no CLI value was supplied. The existing site and home environment handling already matches the requested precedence and path normalization.

Added coverage in [tsh_test.go](/app/tool/tsh/tsh_test.go:659) for Kubernetes selection and CLI priority, and for `TELEPORT_HOME` overriding the CLI value and removing trailing slashes.

Passed: `go test ./tool/tsh -run 'TestReadClusterFlag|TestReadKubeClusterFlag|TestReadTeleportHome'`; `git diff --check`.