Implementer progress: inspecting token accounting, chat/agent flow, and callers; diagnosis remains to be verified.
Verified: plan discards streamed deltas for usage, and usage is embedded in response types. Implementing separate counters and cumulative stream tokenization.
Implemented TokenCount API and per-step prompt/completion accounting; streaming counts re-tokenize cumulative text to handle chunk boundaries. Updated Chat, Assist, web consumers and tests. AI/model tests pass; Assist/web builds blocked by missing native C headers/CGO dependencies.
Final: go test ./lib/ai/model ./lib/ai passed; git diff --check clean. Race build was stopped after prolonged dependency compilation without test output.
