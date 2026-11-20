# Checkpoint

Task: add Amazon Linux 2023/2025/2027/2029 version recognition and EOL support, preserving existing Amazon Linux behavior.

Completed: normalized supported Amazon Linux releases and legacy `YYYY.MM` releases, parsed current Amazon Linux system-release formats, routed OVAL lookups and ALAS advisory links for the newer releases, and added EOL dates for 2023/2025/2027/2029.

Verification: `go test ./config ./scanner ./oval` passed; `git diff --check` passed.
