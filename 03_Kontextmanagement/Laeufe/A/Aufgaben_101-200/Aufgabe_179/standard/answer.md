RemoteCluster now persists its status, last heartbeat, and expiry. Tunnel updates advance the heartbeat in UTC; deleting the newest tunnel cannot move it backward, and deleting the last tunnel sets the cluster Offline while retaining that heartbeat.

Added a regression test for those transitions. `go test ./lib/services/local ./lib/auth` and `git diff --check` passed.