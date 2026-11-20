# Checkpoint

Completed tsh error propagation, runtime configuration callbacks, and SSO login injection. Updated service startup to propagate OS assigned auth, proxy, node, and diagnostic listener addresses. Added focused checks for SSO overrides, tsh returned errors, and dynamic listener ports.

Verification: `go test ./tool/tsh ./lib/client ./lib/service` passed; `git diff --check` passed.
