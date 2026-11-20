Updated Windows SSH stderr handling to replace embedded CLIXML with readable bytes while preserving surrounding text and malformed or incomplete blocks. Tightened the UTF-16-BE escape regex so Unicode lookalikes remain unchanged.

The relevant SSH and PowerShell tests passed: **48 passed**. `git diff --check` also passed.