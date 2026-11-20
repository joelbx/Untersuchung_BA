Progress: Fault localization complete. No project source or tests modified.

Findings:
- lib/ai/chat.go Complete returns (any,error); its predefined greeting embeds zero TokensUsed and its agent branch discards any separate usage result.
- lib/ai/model/agent.go PlanAndExecute returns (any,error) and stores a TokensUsed on the output type. plan creates a completion builder but never appends streaming deltas (comment notes race), then calls AddTokens(prompt, empty string). It also ignores AddTokens errors. Thus each LLM step counts its prompt and only perRequest for completion.
- parsePlanningOutput returns StreamingMessage as soon as it recognizes the final header; a goroutine continues draining deltas after plan returns. Any completion counter must remain live until the stream has finished, with safe synchronization and a defined finalization point.
- lib/ai/model/messages.go has perMessage=3, perRole=1, perRequest=3 and cl100k_base encoding inside TokensUsed.AddTokens, but usage is embedded in Message, StreamingMessage, and CompletionCommand. A separate TokenCount API belongs in lib/ai/model/tokencount.go.
- lib/assist/assist.go ProcessComplete extracts TokensUsed from each response type and returns *TokensUsed. lib/web/assistant.go reads Prompt/Completion fields for rate limiting and usage events; both call sites need migration to the new totals API.
- Existing lib/ai/chat_test.go expects the old two-return Complete signature and embedded usage, and checks stream parts but not streaming completion usage. No model token-counter tests found.

Uncertainty: Streaming API yields text deltas, not token IDs in this code; Add() once per delta would count chunks rather than exact cl100k tokens. Exact final usage requires tokenizing the accumulated completion or a token-aware stream strategy. Error paths need explicit policy for returning the required non-nil TokenCount.
