Updated the Kubernetes proxy so `authenticate` returns `AccessDenied` for access-related `setupContext` failures and preserves the trace classification of other failures. Tests now verify that unknown-cluster and no-reverse-tunnel errors remain non-`AccessDenied`.

Added the two requested `httplib` error-writer wrappers. The full test suites for `lib/kube/proxy` and `lib/httplib` pass.