Implemented gzip response handling.

- Added `GzipDecodedReader` and decompression support across `Request`, `open_url`, `fetch_url`, and `fetch_file`.
- Added default-on `decompress` options to `uri` and `get_url`; setting it to `false` preserves compressed bytes.
- Added automatic `Accept-Encoding: gzip` and missing-gzip deprecation handling.
- Updated existing URL utility assertions for the new defaults.

Validation: URL utility suite passed (**79 tests**), syntax and diff checks passed, and a `Request.open` smoke check verified decoding with an incorrect `Content-Length`.