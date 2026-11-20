Implemented the Kubernetes session uploader initialization and the Forwarder changes.

- The Kubernetes service now starts the file session uploader, which creates the streaming upload directory.
- Forwarder configuration uses the clearer responsibility names, and `ServeHTTP` delegates to its router.
- Audit emissions for `exec`, `portForward`, and `catchAll` use the forwarder lifetime context.
- The Kubernetes TLS server uses `AuthClient` as its heartbeat announcer.

Verification passed: `go test ./lib/kube/proxy` and `go test ./lib/service`. `git diff --check` reported no issues.