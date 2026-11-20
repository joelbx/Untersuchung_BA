Task: Persist RemoteCluster status and heartbeat across tunnel connection changes.
State: Complete.
Changes: Added Presence.UpdateRemoteCluster with backend JSON persistence and expiry. Auth status refresh retains maximum heartbeat, persists changed status, and keeps the last heartbeat when tunnels vanish. Wired method through auth role wrapper and HTTP client/API. Added auth regression test for creation, newer tunnel, intermediate deletion, final deletion, stored status and expiry.
Verification: go test ./lib/services/local ./lib/auth -count=1 passed. git diff --check passed.
