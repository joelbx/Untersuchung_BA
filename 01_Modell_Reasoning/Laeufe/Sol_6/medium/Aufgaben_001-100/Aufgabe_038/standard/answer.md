Implemented transparent gzip decoding in the shared HTTP utility and added the `decompress` option to `uri` and `get_url`. Responses stay compressed when `decompress: false`; decoded streams remain fully readable even when the response carries the compressed `Content-Length`.

Added local HTTP tests and updated existing request expectations. The URL utility suite passed: **87 tests**.