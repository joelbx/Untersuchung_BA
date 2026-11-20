Implemented transparent gzip decoding for HTTP responses in the shared URL utility, with a `decompress` option defaulting to `True` in `uri`, `get_url`, and the URL helper functions. Added `GzipDecodedReader`, preserved response metadata, and added the required missing-gzip deprecation behavior.

Verification: all 85 URL utility tests pass; modified modules compile; `git diff --check` passes.