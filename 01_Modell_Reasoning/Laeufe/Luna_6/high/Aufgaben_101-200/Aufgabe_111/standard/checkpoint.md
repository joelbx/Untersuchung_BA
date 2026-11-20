# Checkpoint

Implemented Amazon Linux release normalization for 1, 2, 2022, 2023, 2025, 2027, and 2029; `YYYY.MM` releases normalize to 1, while unknown releases stay unknown. Added standard support dates for the four requested releases and generalized system-release parsing to detect newer Amazon Linux releases.

Verification: `go test ./config ./scanner` passed.
