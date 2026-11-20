Updated Windows SSH stderr handling to replace embedded, valid CLIXML with readable bytes while preserving surrounding text and incomplete or invalid blocks. The decoder uses UTF-8 with a cp437 fallback, and the UTF-16-BE escape pattern now leaves unrelated Unicode sequences intact.

The relevant PowerShell and SSH tests pass: **49 passed**.