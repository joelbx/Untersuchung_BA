Implemented embedded CLIXML replacement in Windows SSH stderr, with UTF-8 decoding and cp437 fallback. Incomplete or malformed blocks remain unchanged, surrounding stderr is preserved, and the PowerShell escape regex now matches explicit UTF-16-BE hex bytes.

The existing SSH unit tests passed: **18 passed**. `git diff --check` also passed.