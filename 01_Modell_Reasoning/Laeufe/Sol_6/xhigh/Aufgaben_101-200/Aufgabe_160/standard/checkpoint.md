# Checkpoint

Task: Fix Direct Dial node heartbeat addresses that advertise wildcard listeners.

Plan: Trace inventory stream implementations and SSH heartbeat handling, pass the TCP peer address through the upstream stream, rewrite wildcard node addresses while retaining the heartbeat port, then run existing relevant tests.

Status: Implemented `PeerAddr` for gRPC and in-memory upstream streams, added `ICSPipeOption` and `ICSPipePeerAddr`, and rewrote non-routable SSH heartbeat addresses using the peer host before `UpsertNode`.

Verification: Focused API client tests passed; focused and full `lib/inventory` tests passed. `git diff --check` passed. The full API client suite was stopped after it continued for over 90 seconds without output; focused API client tests passed.
