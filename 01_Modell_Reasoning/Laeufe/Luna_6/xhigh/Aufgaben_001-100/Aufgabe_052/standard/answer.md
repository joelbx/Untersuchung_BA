Implemented token accounting across agent steps and streaming responses. `Chat.Complete` and `Agent.PlanAndExecute` now return a non-nil `*model.TokenCount`; Assist and web usage reporting use the aggregate.

Added the cl100k-based counter API in [tokencount.go](/app/lib/ai/model/tokencount.go), updated agent streaming accounting in [agent.go](/app/lib/ai/model/agent.go), and adapted callers and chat tests.

Validation: `go test ./lib/ai/...` passes, and `git diff --check` passes. Assist/web tests could not compile because required system headers and cgo-dependent implementations are unavailable in the container.