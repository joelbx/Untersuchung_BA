Updated Kubernetes proxy `authenticate` to return `AccessDenied` for access-related failures and preserve the trace classification of other setup and authorization errors. Tests now cover the unknown Kubernetes cluster, missing reverse tunnel, unsupported user, and authorization error cases.

`go test ./lib/kube/proxy -count=1` and `git diff --check` passed.