# Checkpoint

Task: fix teleport-kube-agent Kubernetes backend environment configuration.

Status: investigating root cause. `rg` is unavailable (`/bin/sh: rg: not found`); using local `find`/`grep`.

Root cause: `lib/backend/kubernetes/kubernetes.go` defines `namespaceEnv` and `releaseNameEnv` as private constants. Constructor validation and config assignment already use them, but the required exported names do not exist. `teleportReplicaNameEnv` validation is present. Existing Exists/Get/Put tests set namespace conditionally and thus depend on ambient process environment for their missing-variable cases.

Pattern: the constructor reads each environment key from a constant and stores namespace/release in `Config`; backend methods use those config fields. No separate environment lookup occurs in methods.

Hypothesis: exporting the two constants and updating all namespace/release lookups resolves the contract; setting test env vars unconditionally removes ambient-environment dependence. A new focused test was added first. Pre-fix command `GOPROXY=off GOSUMDB=off go test ./lib/backend/kubernetes -run '^TestNewWithClientEnvironment$' -count=1` failed at compile with `undefined: NamespaceEnv` and `undefined: ReleaseNameEnv` (lines 137, 142, 144), as expected.

Patch: exported `NamespaceEnv` and `ReleaseNameEnv`, replaced namespace/release environment lookups with them, and made all backend tests set namespace, replica, and release values explicitly. Added `TestNewWithClientEnvironment` to cover exact constant values, both required-variable errors, config fields, secret name, and Helm annotations.

Verification: `GOPROXY=off GOSUMDB=off go test ./lib/backend/kubernetes -count=1` passed (`ok ... 0.029s`). `git diff --check` passed. No downloads or external research used.
