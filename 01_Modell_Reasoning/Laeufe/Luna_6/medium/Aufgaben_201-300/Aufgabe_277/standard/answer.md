Updated [types.go](/app/internal/server/audit/types.go) to add the JSON-tagged operator fields and map single or multiple segment keys in `NewRule` and `NewRollout`. Multiple keys are comma-separated, with the operator included for multiple segments.

`go test ./internal/server/audit/...` is still running; it produced no output before I stopped waiting.