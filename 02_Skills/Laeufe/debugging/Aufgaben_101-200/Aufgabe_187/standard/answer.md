Fixed the Kubernetes exec failure by initializing the session uploader during Kubernetes service startup, so the streaming upload directory is created automatically.

The forwarder now caches only TLS credentials, rebuilds cluster sessions for each request, keeps audit writes alive after client disconnects, logs exec response errors, and delegates `ServeHTTP` to its internal router. I also updated the config field names and heartbeat announcer.

Verification: `go test ./lib/kube/proxy ./lib/service -count=1` passed. See the [checkpoint](/app/.codex-role-output/checkpoint.md) for the reproduced failure and test record.