Task: Fix PowerShell CLIXML parsing.
Status: Complete. Parser now filters streams, combines entries within each block, separates nonempty blocks with CRLF, decodes UTF-16 escapes including surrogate pairs, and preserves unpaired surrogates in UTF-8 bytes. Existing shell tests pass (7 passed).
