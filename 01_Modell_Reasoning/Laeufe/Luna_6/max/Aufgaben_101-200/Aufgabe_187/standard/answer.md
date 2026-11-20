Implemented the Kubernetes session and forwarder fixes.

- Kubernetes startup initializes the session uploader, creating the streaming upload directories. Initialization is idempotent when multiple services share a process.
- The forwarder now caches only ephemeral credentials, validates that certificates have at least one minute remaining, and serializes CSR requests per authenticated context. Each request gets fresh cluster state.
- Audit events use the service context, and exec completion events are emitted on error paths, including client disconnects. The forwarder also exposes `ServeHTTP()` and uses the renamed configuration fields.

Verification passed: `go test ./lib/kube/proxy ./lib/service` and `git diff --check`. Updated [checkpoint.md](/app/.codex-role-output/checkpoint.md).