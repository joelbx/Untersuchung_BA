Fixed RemoteCluster status and heartbeat persistence. Tunnel updates now keep the latest heartbeat, and removing the final tunnel sets the cluster Offline without clearing it. The new `UpdateRemoteCluster` method preserves resource expiry.

The local presence tests and targeted auth API tests passed; `git diff --check` is clean. The repository work item is complete.