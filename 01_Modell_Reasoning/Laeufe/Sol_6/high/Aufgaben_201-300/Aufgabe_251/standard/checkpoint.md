Task: improve YAML validation diagnostics and command output.
Status: complete. Added Result and FeaturesValidator API; errors include field paths, descriptive messages, and YAML node source coordinates. Text and JSON output use the caller writer; command emits validation failure on stderr and keeps its failure exit code. Added tests for multiple errors, exact locations, formats, multiple files, malformed YAML, and success JSON.
Verification: GOPROXY=off go test ./internal/cue ./cmd/flipt (pass); git diff --check (pass).
Constraints: used local repository only; did not alter git history, index baseline, or harness configuration.
