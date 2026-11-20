# Checkpoint

Task: fix Kubernetes interactive exec session uploader and forwarder request handling.

Changes:
- Initialize the session uploader when the Kubernetes service starts.
- Cache only ephemeral certificates; create routing, transport, and cluster sessions per request. Serialize CSRs for the same authenticated context and reject cached certificates with less than one minute of validity.
- Emit exec, port forward, and catch all audit events using the forwarder context, and preserve final exec audit events if sending status fails.
- Rename forwarder configuration fields, use AuthClient for Kubernetes heartbeat announcements, and delegate ServeHTTP to an internal router.

Verification:
- `go test ./lib/kube/proxy ./lib/service` — passed (both packages).
- `go test -race ./lib/kube/proxy -run '^TestRequestCertificateCachesConcurrentRequests$' -count=1` — passed.
- `git diff --check` — passed.
- Go compiler emitted an existing `github.com/mattn/go-sqlite3` C warning; commands exited 0.
- No live Kubernetes cluster was available for an end to end kubectl exec check.
