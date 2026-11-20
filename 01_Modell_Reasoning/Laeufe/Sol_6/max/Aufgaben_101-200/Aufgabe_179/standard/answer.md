RemoteCluster status is now persisted when the auth service reads it. The update keeps the newest heartbeat in UTC, leaves it intact when the final tunnel is removed, and preserves the cluster’s expiry. `UpdateRemoteCluster` is available through the Presence interface, local storage, and auth API.

The relevant local and auth CRUD and lifecycle tests passed: 3 tests in each package.