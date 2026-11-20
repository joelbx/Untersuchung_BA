# Checkpoint

Task: expose canonical default config and decode hooks, keep production decoding aligned, and pass config schema validation.
Status: implemented and verified.
Changes: exported DecodeHooks; added DefaultConfig through the shared load/default path; kept Load on the exported hooks; tagged version for mapstructure; changed Storage Local and Git to pointers with nil-safe validation; updated storage expectations and added a default parity assertion.
Verification: go test ./internal/config ./internal/cue ./internal/cmd (passed).
