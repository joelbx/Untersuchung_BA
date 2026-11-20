# Checkpoint

Implemented Amazon Linux release normalization for 1, 2, 2022, 2023, 2025, 2027, and 2029, with YYYY.MM mapped to 1 and other releases mapped to unknown. Added EOL dates and boundary tests, updated `/etc/system-release` detection for year-based releases, and added ALAS2023 advisory links.

Verification: `GOPROXY=off GOSUMDB=off go test ./config ./scanner ./oval` passed. `git diff --check` passed. `rg` was unavailable; searches used `grep`.
