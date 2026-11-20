Task: Add transparent gzip response handling for `uri`, `get_url`, and shared URL utilities.

Progress: Implemented `GzipDecodedReader`, response decoding (including HTTP errors), request header defaults,
and `decompress` propagation through shared URL helpers and the `uri` and `get_url` modules.
Updated existing URL utility tests and added stream, header, and missing gzip coverage.

Verification: `pytest -q test/units/module_utils/urls` passed (88 tests). A local HTTP smoke test
decoded 12,000 bytes from a 76 byte gzip response with the compressed Content-Length header.
`python -m compileall` and `git diff --check` passed.
