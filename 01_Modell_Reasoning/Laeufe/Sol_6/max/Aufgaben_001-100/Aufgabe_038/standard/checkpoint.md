# Checkpoint

Task: transparent gzip decoding for shared HTTP utilities and `uri`/`get_url`.

Completed: implemented `GzipDecodedReader` with response metadata and resource cleanup; added automatic `Accept-Encoding`, request default fallback, and `decompress` propagation through `open_url`, `fetch_url`, `fetch_file`, `uri`, and `get_url`. Missing gzip support produces an actionable direct error; `fetch_url` disables decompression and deprecates with version `2.16`. Bodyless HEAD/204/304 responses bypass decoding. Added regression coverage for compressed and plain streams, opt-out, Content-Length, lowercased headers, HTTP errors, missing gzip, and module-facing behavior.

Verification: `PYTHONPATH=lib:test/units python -m pytest -q test/units/module_utils/urls` passed (98 tests); `git diff --check` passed.
