Migrated `get_ia.py` from urllib to requests. The request helper now accepts headers and keyword arguments, validates HTTP status, and returns a response. Callers use `.content` for binary data and `.text` for text, with UTF-8 as the default when no charset is declared.

Updated the catalog tests for response objects, retries, status errors, decoding, and range headers. **49 tests passed.**