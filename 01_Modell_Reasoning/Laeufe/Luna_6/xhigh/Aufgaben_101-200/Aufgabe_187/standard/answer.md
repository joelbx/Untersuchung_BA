Implemented the Kubernetes exec and Forwarder fixes.

- Kubernetes-only startup initializes the session uploader and its streaming directories in [kubernetes.go](/app/lib/service/kubernetes.go:201).
- The Forwarder caches fresh Kubernetes credentials, rebuilds request-scoped sessions, preserves audit writes after client disconnects, and logs exec failures in [forwarder.go](/app/lib/kube/proxy/forwarder.go:63).
- Added `ServeHTTP` routing and wired the TLS heartbeat announcer to `AuthClient`.

Verified: `go test ./lib/kube/proxy ./lib/service ./lib/events/filesessions` passed; `git diff --check` passed.