# Checkpoint

Task: Fix Windows stderr handling for embedded CLIXML sequences.

Completed:
- Tightened UTF-16-BE serialized string matching to require null-byte/hex-byte pairs.
- Added byte-preserving CLIXML replacement for embedded, complete stderr blocks, with UTF-8 and cp437 decoding paths.
- Kept malformed and incomplete blocks unchanged and wired the helper into Windows SSH command execution.
- Ran the existing PowerShell and SSH unit modules (35 passed), targeted CLIXML smoke checks, and `git diff --check`.
