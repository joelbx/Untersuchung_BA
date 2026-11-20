Task: Preserve RemoteCluster status and last heartbeat across tunnel connection changes.
Progress: Added Presence.UpdateRemoteCluster storage and auth/API implementations. Auth status reads persist changes, retain the maximum heartbeat in UTC, and set Offline after the last tunnel disappears. Added local expiry and auth transition tests.
Verification: Focused RemoteCluster and tunnel CRUD tests pass in lib/services/local and lib/auth; cache tunnel test passes. git diff --check passes.
