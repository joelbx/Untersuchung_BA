Updated Windows SSH stderr handling to replace complete embedded CLIXML blocks with readable text while preserving surrounding bytes and incomplete or invalid blocks. CLIXML decoding now falls back from UTF-8 to cp437, and the UTF-16-BE escape matcher preserves Unicode lookalikes.

Verification: 44 relevant unit tests passed; `git diff --check` passed.