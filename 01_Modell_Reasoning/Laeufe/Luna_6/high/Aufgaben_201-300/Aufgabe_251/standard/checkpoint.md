# Checkpoint

Implemented the validator API (`Result`, `FeaturesValidator`, `NewFeaturesValidator`, and `Validate`) and updated CLI file validation to aggregate issues across inputs. Errors now carry a field path, a descriptive CUE message, and source coordinates resolved from the original YAML nodes. JSON and text output use the supplied writer; failures return `ErrValidationFailed`.

Verification completed:
- `go test ./internal/cue ./cmd/flipt`
- Manual `flipt validate -F json` checks confirmed exact per-key locations for multiple misspelled fields, a rollout range error at its value, and exit status 1.
- `git diff --check`
