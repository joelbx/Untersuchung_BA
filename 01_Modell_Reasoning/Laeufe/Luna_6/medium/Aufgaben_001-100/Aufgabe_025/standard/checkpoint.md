# Checkpoint

Issue: support exact `${VARIABLE_NAME}` references in YAML configuration through the existing decode-hook pipeline.

Plan: inspect `internal/config` loading and its existing hooks; add a string substitution hook that only resolves valid exact references present in the environment; ensure it runs before type conversions; add focused tests for valid, invalid, missing, and multiple references; run relevant existing Go tests.
