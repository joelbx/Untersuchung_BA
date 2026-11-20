RemoteCluster now persists its connection status and last heartbeat. Removing a newer tunnel no longer moves the heartbeat backward; removing the final tunnel sets the status to Offline while retaining that heartbeat. The update also preserves the cluster’s expiry.

Verification: `go test ./lib/services/local ./lib/auth -count=1` and `git diff --check` passed.