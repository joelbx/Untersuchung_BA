Windows SSH stderr now replaces valid embedded CLIXML blocks with readable UTF-8 bytes, using cp437 when UTF-8 decoding fails. Surrounding text and malformed or incomplete blocks remain unchanged. The UTF-16-BE escape matcher was also corrected to preserve valid Unicode escape text.

The relevant existing tests pass: **46 passed**.