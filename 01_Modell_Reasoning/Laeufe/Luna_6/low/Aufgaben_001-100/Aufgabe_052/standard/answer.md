Implemented token accounting with `cl100k_base`, including prompt and streamed completion counts accumulated across agent steps. `Chat.Complete` and `Agent.PlanAndExecute` now return a non-nil `*model.TokenCount`, and legacy response token fields remain populated.

Updated the existing chat tests for the new return signature. **Validation passed:** `go test ./lib/ai/...`.