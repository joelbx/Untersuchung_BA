Implemented token accounting for `Chat.Complete` and `Agent.PlanAndExecute`. Both now return a non-nil `*model.TokenCount`; the agent accumulates prompt and completion counts across steps, including streamed responses. Assist and web usage reporting now read those totals.

`go test ./lib/ai/model ./lib/ai` passed, and `git diff --check` was clean. `go test ./lib/assist` could not build because this environment lacks required native C headers and has SQLite C compilation errors.

No delegation was used.