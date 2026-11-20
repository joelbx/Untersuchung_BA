# Checkpoint

Implemented Amazon Linux release parsing for versions 1, 2, 2022, 2023, 2025, 2027, and 2029. Legacy `YYYY.MM` strings resolve to release 1; unknown versions resolve to `unknown`. Scanner detection now extracts newer Amazon Linux release identifiers. Added EOL dates and regression tests for recognition, unsupported versions, and support boundary behavior.

Verification: `go test ./config ./scanner` passed.
