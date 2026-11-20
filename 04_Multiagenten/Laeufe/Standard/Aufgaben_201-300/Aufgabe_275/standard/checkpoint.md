Task: Preserve Kubernetes proxy authentication error classifications.
Current state: Updated Forwarder.authenticate to preserve non-access errors from authorization and context setup. Added explicit access classifications to TestAuthenticate, including a non-access authorization error. Added the requested httplib error-writer wrappers. Final package tests passed: go test ./lib/kube/proxy ./lib/httplib. git diff --check passed.
Constraints: Keep setupContext's no-tunnel BadParameter classification; run relevant existing tests.
