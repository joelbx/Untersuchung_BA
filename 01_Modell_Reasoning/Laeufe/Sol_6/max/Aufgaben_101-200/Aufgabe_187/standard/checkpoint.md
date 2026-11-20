# Kubernetes forwarder issue checkpoint

- Goal: initialize the Kubernetes session uploader, fix forwarder routing/credentials/audit behavior, and verify with existing tests.
- Repository: `/app`; work is in the checked-out files.
- Initial inspection found `lib/kube/proxy/forwarder.go` and related proxy tests. No `AGENTS.md` was found.
- Found the async streamer at `lib/kube/proxy/forwarder.go` and the uploader initializer at `lib/service/service.go`. Kubernetes service startup omitted the initializer.
- Implemented explicit `Forwarder` router and config, renamed responsibility-specific config fields, moved audit emission to the forwarder context, and changed the cache to hold only short lived TLS credentials with a one minute validity floor.
- Wired Kubernetes startup to initialize the uploader before serving and switched TLS heartbeats to `AuthClient`.
- Completed: Kubernetes service invokes the uploader initializer before serving; uploader initialization is shared once across roles. Forwarder uses explicit config/router, request-scoped sessions, a TTL credential cache with a one minute certificate validity floor, and the forwarder context for audit emission. Exec records stream failures and logs response status errors.
- Verification: `GOPROXY=off go test -mod=vendor ./lib/kube/proxy ./lib/service` passed; focused proxy race tests passed; `GOPROXY=off go test -mod=vendor -run '^$' ./integration` compiled. The live Kubernetes suite requires a configured external Kubernetes cluster and was not run.
- Final review: `git diff --check` passed. Changes are in checked-out files; git index and history were untouched.
