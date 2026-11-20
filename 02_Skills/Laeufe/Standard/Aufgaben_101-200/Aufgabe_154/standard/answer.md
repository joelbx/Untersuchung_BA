Updated Windows SSH stderr handling so complete embedded CLIXML blocks become readable bytes, with UTF-8 decoding and a cp437 fallback. Surrounding bytes and malformed or incomplete blocks remain unchanged. I also corrected the UTF-16-BE escape regex.

Verification: 50 relevant unit tests passed, and `git diff --check` passed.