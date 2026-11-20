# Checkpoint

Task: add transparent gzip response handling across `urls.py`, `uri`, and `get_url`.

Initial repository status: clean. `rg` is unavailable (`/bin/bash: rg: command not found`), so file discovery uses `git ls-files` and text search uses `grep`.

Implemented gzip response decoding in `Request.open` with a `GzipDecodedReader` stream that delegates HTTP metadata and closes the underlying response. The shared URL functions and `uri`/`get_url` expose and forward `decompress`; requests advertise gzip or identity when the caller has not set `Accept-Encoding`. Gzip HTTP error bodies are decoded. When gzip is unavailable, direct Request use raises `MissingModuleError`; `fetch_url` deprecates and disables decoding.

Verification:
- `python -m pytest -q test/units/module_utils/urls` passed before the final import-order and test-assertion edits: 87 passed, 3 existing SSL deprecation warnings.
- A prior run of the same command failed in `test_fetch_url_gzip_http_error` because `HTTPError.read` retained the original stream's bound method; fixed by binding it to the decoded reader and reran successfully.
- Final verification: `python -m pytest -q test/units/module_utils/urls` exited 0 with 87 passed and 3 existing SSL deprecation warnings. `git diff --check` and `python -m compileall -q lib/ansible/module_utils/urls.py lib/ansible/modules/uri.py lib/ansible/modules/get_url.py` both exited 0.
