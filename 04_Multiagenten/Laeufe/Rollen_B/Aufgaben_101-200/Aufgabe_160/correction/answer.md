The Direct Dial fix is in the checked-out patch: upstream streams expose `PeerAddr()`, pipe options can supply it, and SSH heartbeats use the peer’s host for wildcard or local addresses while preserving the heartbeat port.

I also changed the API client test listeners to bind to loopback. The focused API and inventory tests, full inventory suite, and full API client suite now pass. `git diff --check` passes.

**TEST_ENVIRONMENT_PROBLEM:** The separate `/app/api` test command cannot start because `github.com/gogo/protobuf@v1.3.2` is missing from its local cache and downloads are disabled.