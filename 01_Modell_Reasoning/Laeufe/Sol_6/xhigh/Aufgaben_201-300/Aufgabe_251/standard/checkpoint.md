# Validation issue checkpoint

Task: improve YAML validation diagnostics and `flipt validate` output.
Status: implementation complete; focused tests pass.
Changes: structured Result API with all CUE errors, field paths, source file/line/column selection and decoder column correction; missing-field and malformed-YAML handling; JSON/text command output and stderr failure message.
Verification: `go test ./internal/cue ./cmd/flipt` passes; manual JSON CLI run reports the rollout field at line 17, column 16 and exits with failure; `git diff --check` passes.
Constraints: local code/tests only; git history, index, and harness configuration untouched.
