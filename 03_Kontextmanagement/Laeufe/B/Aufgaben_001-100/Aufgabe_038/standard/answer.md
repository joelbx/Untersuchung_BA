Implemented gzip response handling in `urls.py` and added a `decompress` option, defaulting to `True`, to `uri` and `get_url`. Requests can now return decoded content or preserve compressed bytes when decompression is disabled.

Verification passed: **12 URL utility tests**, local gzip and plain HTTP response checks, syntax compilation, and `git diff --check`.