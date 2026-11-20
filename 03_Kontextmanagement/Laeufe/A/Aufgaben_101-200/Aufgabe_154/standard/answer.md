Fixed Windows SSH stderr handling so valid CLIXML blocks are replaced with readable UTF-8 bytes, with cp437 fallback. Surrounding text and incomplete or invalid blocks are preserved. The UTF-16-BE escape match is also narrower, preserving literal Unicode sequences.

The relevant PowerShell and SSH tests pass: **48 passed**.