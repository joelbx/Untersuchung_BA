# Checkpoint

Objective: Fix Direct Dial SSH node heartbeats that publish wildcard addresses.

Implemented: upstream inventory control streams expose the TCP peer address; in-memory stream pipes accept ICSPipePeerAddr; the inventory controller substitutes the peer host for local or wildcard SSH addresses before UpsertNode, retaining the node port.

Verification: targeted API client stream tests pass through the root module; the full lib/inventory suite passes. The full API client suite was stopped after more than 90 seconds with no result. git diff --check passes.
