# Checkpoint

Task: preserve Kubernetes proxy authentication error classifications.

Changes:
- `authenticate` retains `AccessDenied` for access-related authorization and context failures.
- Other authorization and `setupContext` failures are returned with `trace.Wrap`, preserving their trace classification.
- `TestAuthenticate` checks access-denied and bad-parameter classifications for authorization, unsupported user, unknown local Kubernetes cluster, and remote cluster without a tunnel.

Verification:
- `gofmt -w lib/kube/proxy/forwarder.go lib/kube/proxy/forwarder_test.go` completed.
- `git diff --check` passed.
- `GOPROXY=off GOSUMDB=off go test ./lib/kube/proxy -run '^TestAuthenticate$' -count=1` passed.
- `GOPROXY=off GOSUMDB=off go test ./lib/kube/proxy -count=1` passed after final test edit.

Note: `rg` is unavailable (`/bin/bash: rg: command not found`), so local `grep`/`find` were used.
