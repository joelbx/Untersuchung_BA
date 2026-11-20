# Checkpoint

Completed Kubernetes forwarder and service fix.

- Kubernetes service initializes the uploader before serving requests, creating the async streaming directory.
- Forwarder uses named config dependencies, explicit ServeHTTP routing, server context for audit emission, and rebuilt request sessions with a TTL cache containing only certificates.
- Credential requests are serialized per authenticated key and cache entries require at least one minute of remaining certificate validity.
- Exec records audit outcomes even when streaming or response status fails.

Verification: `go test ./lib/kube/proxy ./lib/service` passed; `git diff --check` passed.
