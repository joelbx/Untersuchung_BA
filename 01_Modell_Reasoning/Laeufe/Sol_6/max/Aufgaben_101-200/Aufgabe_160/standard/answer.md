Direct Dial SSH heartbeats now replace wildcard or local node hosts with the inventory stream’s peer host before `UpsertNode`, while preserving the node’s original port. I also added `PeerAddr()` and the `ICSPipePeerAddr` pipe option.

The focused API client tests and full `lib/inventory` suite pass. The broader API client suite was stopped after more than 90 seconds without a result.