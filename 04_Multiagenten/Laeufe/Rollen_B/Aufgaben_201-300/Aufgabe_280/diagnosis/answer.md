The likely fix is in [kubernetes.go](/app/lib/backend/kubernetes/kubernetes.go:37): `namespaceEnv` and `releaseNameEnv` have the required values but are private. Export them as `NamespaceEnv` and `ReleaseNameEnv`, then use those names throughout the backend.

`NewWithClient()` already checks both required variables and produces the specified error text. It also populates `Config.Namespace` and `Config.ReleaseName` from the correct environment variables. `Exists()`, `Get()`, and `Put()` use that configuration downstream, so I found no separate fault in those methods.

The [existing tests](/app/lib/backend/kubernetes/kubernetes_test.go:25) use the private namespace constant and do not assert the exact missing-variable error or release-name annotations. Their missing-variable cases may also depend on inherited environment values because they skip setting empty variables.

I recorded the findings in `.codex-role-output/checkpoint.md`. I did not edit project source or tests under this run’s fault-localization scope, and I did not run tests.