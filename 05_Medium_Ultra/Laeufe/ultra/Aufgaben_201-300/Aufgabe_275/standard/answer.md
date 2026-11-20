Updated [authenticate](/app/lib/kube/proxy/forwarder.go:316) so access-related failures remain `AccessDenied`, while lookup and setup failures retain their original trace classification. The no-tunnel `BadParameter` in `setupContext` is unchanged.

Added the requested [httplib error-writer wrappers](/app/lib/httplib/httplib.go:44) and classification tests. Two subagents handled the proxy tests and httplib wrappers; I reviewed the combined changes.

Verification passed: `GOPROXY=off GOSUMDB=off go test -mod=vendor ./lib/httplib ./lib/kube/proxy`.