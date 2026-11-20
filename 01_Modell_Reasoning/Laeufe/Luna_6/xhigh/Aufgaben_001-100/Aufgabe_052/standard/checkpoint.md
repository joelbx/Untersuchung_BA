# Checkpoint

Task: implement token accounting for `Chat.Complete` and `Agent.PlanAndExecute` in `/app`.

Implementation complete:
- Added exported token counter interfaces and constructors using `cl100k_base`, including a finalizable asynchronous stream counter.
- Agent calls now return a non-nil aggregate and accumulate prompt/completion usage for each planning step; streamed completion text is recounted across fragment boundaries.
- `Chat.Complete` returns `(any, *model.TokenCount, error)`; Assist and web usage reporting consume the aggregate.
- Updated existing chat tests for the new return type.

Validation:
- `go test ./lib/ai/...` passes.
- `git diff --check` passes.
- Wider Assist/web test runs cannot compile in this container because external C/system dependencies are unavailable (`linux/hidraw.h`, `gnu/libc-version.h`, and cgo-dependent packages); disabling CGO also fails due missing cgo-only implementations.
