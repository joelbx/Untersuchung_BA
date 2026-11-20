# Checkpoint

Task: Fix Direct Dial SSH node heartbeats advertising wildcard addresses.
Implemented: upstream control streams expose TCP peer addresses; in-memory pipes accept peer address options; controller replaces local or wildcard heartbeat hosts with the peer host while preserving the heartbeat port before UpsertNode.
Added tests for pipe peer address and heartbeat address handling.
Verification: gofmt and git diff --check passed. Full `GOPROXY=off go test ./lib/inventory -count=1` passed. `api` module tests could not start offline because github.com/gogo/protobuf@v1.3.2 is uncached.
Delegation: none.
