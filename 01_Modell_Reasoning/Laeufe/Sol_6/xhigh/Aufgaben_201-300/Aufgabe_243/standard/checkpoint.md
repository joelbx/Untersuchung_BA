# Checkpoint

Task: Resolve Kubernetes proxy session endpoint selection and credential handling in `lib/kube/proxy/forwarder.go`.

Initial state: working tree clean; no `AGENTS.md` found. `rg` is unavailable, so searches use `grep` and `find`.

Implemented: `newClusterSession` rejects missing cluster names; local credentials take precedence over service discovery; remote and kube_service sessions use `kubeClusterEndpoint` and `teleportClusterClient.dialEndpoint`; session dialing records the selected `kubeAddress` for request URLs and audit fields. Added tests for missing/unknown clusters, discovery failure with local credentials, authentication context propagation, reverse tunnel dialing, empty endpoints, and endpoint failover.

Verification: `GOPROXY=off GOSUMDB=off go test ./lib/kube/proxy -count=1` passed after the final changes; `git diff --check` passed. The working tree contains only the proxy implementation and test edits (the checkpoint file is ignored by Git).
