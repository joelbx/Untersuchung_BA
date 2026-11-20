# Validation issue checkpoint

- Task: improve `flipt validate` error paths, messages, source coordinates, aggregation, and output.
- Assigned process: systematic debugging. Investigation underway; no fix attempted yet.
- Repository initially clean at commit `54e188b`.
- `rg` is unavailable (`/bin/bash: rg: command not found`); using local `find` and `grep`.

## Investigation

- Existing `validate` uses `yaml.Extract("", b)` and `ValidateFiles` always selects `InputPositions()[0]`. CUE's first position can be a schema location for unknown fields; the YAML position follows it. The code also discards `m.Path()` and stores only `m.Msg()`, producing generic messages.
- Reproduction (`go test ./internal/cue -run TestDiagnostic -v`) shows three errors: `flags.0.ey`, `flags.0.nabled`, and `flags.0.rules.0.distributions.0.rollout`. For unknown keys CUE inputs begin at `7:8` (schema), then `sample.yaml:2:4` or `sample.yaml:4:4`. The range error has `sample.yaml:11:17` first. Thus selecting a position by source filename is necessary.
- The diagnostic test initially failed to compile due to a missing `cue` import; corrected before gathering results. Baseline `go test ./internal/cue` passed.
- Hypothesis: pass the filename into YAML extraction, use CUE's error path for fields, and choose the input position belonging to that file. This should preserve all errors in the returned result and allow both output modes to show them.

## Implementation and verification

- Added `Result`, `FeaturesValidator`, and `NewFeaturesValidator`; `Validate` returns all CUE errors with their paths and source positions. `ValidateFiles` uses the structured result for text and JSON output and writes JSON to its supplied writer.
- The regression test failed before the fix with two `field not allowed` messages both at line 7, column 8. It passes after the fix with the `ey` and `nabled` fields at lines 2 and 4.
- A YAML syntax error from CUE's YAML parser provides a line in its error text but no token position or column. The validator extracts the line and uses column 1 as a fallback; the exact syntax error column remains unavailable from this parser.
- `go test ./internal/cue ./cmd/flipt -count=1` passed (the command package has no tests). `go run ./cmd/flipt validate -F json internal/cue/fixtures/invalid.yaml` returned exit status 1 and JSON with the rollout field, bound, and source location. `git diff --check` passed.
