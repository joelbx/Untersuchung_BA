Updated Windows SSH stderr handling to replace embedded CLIXML with readable UTF-8 bytes, using cp437 when UTF-8 decoding fails. Surrounding output and incomplete or invalid blocks remain unchanged. I also corrected the UTF-16-BE escape regex.

Verification: 49 relevant unit tests passed; `git diff --check` passed.