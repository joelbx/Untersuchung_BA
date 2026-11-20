Updated `authenticate` to return `AccessDenied` for access-related setup failures and wrap other errors, preserving their trace classification. Updated `TestAuthenticate` to check authorization and unsupported-user denials, plus `BadParameter` for unknown clusters and requests without a reverse tunnel.

Verification passed: `go test ./lib/kube/proxy -run '^TestAuthenticate$' -count=1`.