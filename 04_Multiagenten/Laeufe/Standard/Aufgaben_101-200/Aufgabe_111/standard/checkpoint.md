# Checkpoint

Completed Amazon Linux 2023/2025/2027/2029 version normalization and EOL mappings, including dated patch releases. Updated system release detection, OVAL release lookup, ALAS2023 advisory links, and package dependency checks for newer Amazon Linux. Added the correctly spelled extended support check while retaining the prior spelling for compatibility. Added focused regression tests. Verified with `GOPROXY=off GOSUMDB=off go test ./config ./oval ./scanner ./models` (all passed) and `git diff --check`.
