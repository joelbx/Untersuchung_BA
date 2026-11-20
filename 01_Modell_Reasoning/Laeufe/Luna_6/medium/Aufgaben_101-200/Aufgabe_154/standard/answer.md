Implemented embedded CLIXML decoding for Windows SSH stderr, preserving surrounding bytes and leaving incomplete or invalid blocks unchanged. Updated the UTF-16-BE escape matcher.

The existing PowerShell and SSH unit tests passed: **35 passed**. `git diff --check` passed.