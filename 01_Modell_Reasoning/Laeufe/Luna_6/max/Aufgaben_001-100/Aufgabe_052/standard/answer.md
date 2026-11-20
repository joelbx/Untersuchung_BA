Implemented token accounting for chat and agent executions.

- Added the `cl100k_base` counter API and streaming counter in [tokencount.go](/app/lib/ai/model/tokencount.go).
- Updated [Chat.Complete](/app/lib/ai/chat.go:60) and [Agent.PlanAndExecute](/app/lib/ai/model/agent.go:100) to return a non-nil `*model.TokenCount`. Prompt and completion counts accumulate across agent steps, including streamed text.
- Updated Assist and existing callers for the new API. Updated the AI test expectations to include generated action tokens.

Verification: `go test ./lib/ai/... -count=1` passed; `git diff --check` passed. Assist tests could not build in this container because required C headers and cgo-backed system APIs are unavailable. The checkpoint is recorded in [.codex-role-output/checkpoint.md](/app/.codex-role-output/checkpoint.md).