Task: Add exact `${VARIABLE_NAME}` substitution to YAML configuration values before other decode hooks.
Status: Added exact-match environment substitution as first decode hook and tests for matching, non-matching, missing, multiple references, type conversion, and FLIPT override precedence.
Verification: `go test ./internal/config -count=1` and `go test ./config -count=1` passed; `git diff --check` passed.
Constraints: Use local code/tests only; keep git history, index baseline, and harness configuration unchanged.
