Updated the Windows SSH stderr path to replace complete CLIXML blocks with decoded text while preserving surrounding bytes and incomplete or invalid blocks. It now tries UTF-8 first, then cp437. I also corrected the UTF-16-BE escape matcher so valid Unicode sequences remain intact.

Verification: 51 relevant unit tests passed, and `git diff --check` passed.