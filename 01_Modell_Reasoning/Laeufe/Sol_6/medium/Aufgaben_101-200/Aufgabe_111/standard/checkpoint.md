# Checkpoint

Task: support Amazon Linux 2023 and later release detection and EOL mapping.
Status: implemented and verified.
Changes: normalized known Amazon Linux versions; added EOL dates for 2023, 2025, 2027, and 2029; added Amazon Linux 2023 system-release parsing and ALAS2023 advisory links; added version and EOL boundary tests.
Verification: GOPROXY=off GOSUMDB=off go test ./config ./scanner ./oval (all passed); git diff --check passed.
