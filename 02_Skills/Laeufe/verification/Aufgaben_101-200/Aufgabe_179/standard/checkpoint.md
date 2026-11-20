# Checkpoint

Issue: RemoteCluster status and last heartbeat were recomputed from remaining tunnel connections, causing heartbeat regression after tunnel deletion.

Changes:
- Added `Presence.UpdateRemoteCluster(ctx, rc)` and local backend persistence under `remoteClusters/<name>` with the resource expiry.
- Status refresh now retains the greatest recorded heartbeat in UTC, updates online/offline status, and persists changes.
- Wired the new interface method through the role checked auth wrapper and HTTP client/server.
- Added auth lifecycle coverage for creation, update, partial deletion, final deletion, list results, and stored values; added local expiry coverage and shared client update coverage.

Verification:
- `go test ./lib/services/local ./lib/auth -count=1`: passed (both packages; final run).
- `git diff --check`: passed (final run).
- Initial focused test compile failed because `AuthWithRoles` and `Client` did not implement the expanded `Presence` interface; both were implemented and final tests passed.
- `rg` unavailable (`/bin/bash: rg: command not found`); local searches used `grep`/`find`.
