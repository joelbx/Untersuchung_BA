Fixed the Direct Dial heartbeat path. Upstream inventory streams now expose `PeerAddr()`, and the in-memory pipe accepts `ICSPipePeerAddr`. When a heartbeat advertises a wildcard or loopback host and a peer address is available, the controller uses the peer host for `UpsertNode` while preserving the SSH port.

I delegated the stream changes, controller changes, and call-site audit, then reviewed and verified the combined patch. The inventory tests, focused API client tests, and `git diff --check` passed. The broader API client suite was stopped after two minutes without a result.

In-process streams have no TCP peer by default, so this rewrite applies when a peer address is available or supplied through the pipe option.