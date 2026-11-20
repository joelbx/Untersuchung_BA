Updated Windows SSH stderr handling to replace valid CLIXML blocks with readable text while preserving surrounding bytes and malformed or incomplete blocks. The decoder uses UTF-8 with a cp437 fallback, and the UTF-16-BE escape matcher now leaves Unicode lookalikes unchanged.

The relevant tests pass: **48 passed**.