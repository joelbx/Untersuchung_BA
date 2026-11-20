# Checkpoint

Implemented configurable protocol, HTTP/HTTPS ports, certificate/key config, HTTPS prerequisite validation, YAML/environment loading over documented defaults, scalar/list CORS origins, and TLS listeners for REST/UI and gRPC. Updated startup callers to pass the config path.

Verification: `git diff --check` passes. `go test ./cmd/flipt` is running but has not returned output yet.
