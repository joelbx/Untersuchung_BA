# Checkpoint

## Task
Resolve token accounting for `Chat.Complete` and `Agent.PlanAndExecute`.

## Implemented
- Added the exported token counter API in `lib/ai/model/tokencount.go`, using `cl100k_base` and the per message, per role, and per request constants.
- Changed chat and agent completion methods to return a non-nil `*model.TokenCount` aggregate.
- Counted prompt and generated completion tokens for each planning step. Streamed output is re-tokenized cumulatively so token boundaries across chunks are accurate.
- Updated Assist and in-repository callers to use the separate aggregate.
- Updated existing AI test expectations to include generated action response tokens.

## Verification
- `go test ./lib/ai/... -count=1`: passed.
- `go test ./lib/ai/model`: passed (package has no test files).
- `go test ./lib/ai/... ./lib/assist`: could not build due unavailable system C headers and SQLite C symbols (`linux/hidraw.h`, `gnu/libc-version.h`, `pread64`/`pwrite64`).
- `CGO_ENABLED=0 go test ./lib/assist`: also could not build; dependencies require cgo-provided HID, PKCS#11, SQLite, and libc metadata APIs.
