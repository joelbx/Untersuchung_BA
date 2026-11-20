Fixed Direct Dial node addresses. Upstream inventory streams now expose `PeerAddr()`, and the in-memory pipe accepts `ICSPipePeerAddr`. When an SSH heartbeat reports a wildcard or local host, the controller uses the peer’s host for `UpsertNode` while preserving the node’s original port.

Focused API and inventory tests pass. The full API client suite was stopped after an extended silent run.