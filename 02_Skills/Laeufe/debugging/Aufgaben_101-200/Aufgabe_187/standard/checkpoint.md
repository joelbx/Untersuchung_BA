# Checkpoint

Task: repair Kubernetes forwarder interactive exec and related lifecycle, caching, and audit behavior.

Status: investigating root cause. `rg` is unavailable (`/bin/bash: rg: command not found`); using local grep/find. No code changes yet.

Root cause: `initKubernetesService` omits `initUploaderService`, while `newStreamer` uses filesessions under the uploader streaming directory. Forwarder caches entire clusterSession, preserving request dialer/remote Site and cluster selection beyond request lifetime. Audit calls use cancelable request context. Existing analogous uploader setup is in service.go.

Hypothesis: initializing uploader during Kubernetes service startup creates the missing path; caching only TLS credentials lets each request rebuild current dialer and endpoint, while detached audit context survives client cancellation.

Implementation: Kubernetes service now calls `initUploaderService` before serving, which creates the streaming upload directory. Forwarder uses named config responsibilities, an internal router with ServeHTTP, service-scoped audit contexts, and a credential-only TTL cache. Per-request cluster sessions are rebuilt, so remote Site and dialer state is not retained. Certificate reuse requires NotAfter at least one minute ahead; concurrent CSR requests for the same key are serialized. Exec errors are logged on return.

Verification:
- Before fix: `go test ./lib/kube/proxy -run 'Test/TestGetClusterSession' -count=1` failed as intended: cached session retained previous teleport cluster name (`site a` instead of empty).
- After fix: `go test ./lib/kube/proxy ./lib/service -count=1` passed (both packages).
- `git diff --check` passed.
- Compiler emits an existing warning from vendored sqlite3-binding.c (`function may return address of local variable`); tests still exit 0.
