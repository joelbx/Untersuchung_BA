# Checkpoint

Implemented:
- Renamed ForwarderConfig responsibilities to Authz, AuthClient, CachingAuthClient, ReverseTunnelSrv, and ConnPingPeriod, with call sites updated.
- Added Forwarder.ServeHTTP delegating to the httprouter router (including its configured NotFound handling).
- Changed exec, portForward, and catchAll audit emissions and the session audit writer to use the forwarder lifetime context.
- Initialized the file session uploader during dedicated Kubernetes service startup, creating the async streaming directory.
- Changed the Kubernetes TLS heartbeat announcer to use ForwarderConfig.AuthClient.

Verification: `go test ./lib/kube/proxy` and `go test ./lib/service` passed.
