Task: improve flipt validate YAML error precision and structured reporting.
Status: complete.
Changes: added FeaturesValidator/Result API; aggregate all CUE findings with field paths, descriptions, and YAML source positions; write text or JSON to the supplied command writer; preserve failure exit status; added validation and format tests.
Verification: go test ./internal/cue ./cmd/flipt -count=1; git diff --check; CLI JSON run on invalid fixture returned error details and exit status 1.
Constraints observed: local code/tests only; no git history, index, or harness changes.
