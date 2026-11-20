Added `TELEPORT_KUBE_CLUSTER` handling to `tsh`; it fills `KubernetesCluster` only when the CLI did not specify one ([tsh.go](/app/tool/tsh/tsh.go:275), [tsh.go](/app/tool/tsh/tsh.go:2285)).

The existing handlers already implement the requested site precedence and `TELEPORT_HOME` override with path normalization.

Verification: `go test ./tool/tsh` passed.