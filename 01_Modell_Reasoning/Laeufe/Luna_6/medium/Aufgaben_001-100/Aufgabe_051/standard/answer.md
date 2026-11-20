Implemented `TELEPORT_KUBE_CLUSTER` support in [tsh.go](/app/tool/tsh/tsh.go). The environment value is used when no Kubernetes cluster was specified on the CLI; CLI values keep precedence. Existing site selection prefers `TELEPORT_CLUSTER` over `TELEPORT_SITE`, with a CLI `SiteName` taking precedence. `TELEPORT_HOME` continues to override CLI `HomePath` and is normalized with `path.Clean`.

Added tests for Kubernetes cluster precedence and environment home override. The focused tests passed:

`go test ./tool/tsh -run 'Test(ReadClusterFlag|ReadKubeCluster|ReadTeleportHome)$'`

`git diff --check` passed.