# Checkpoint

Investigating gzip response handling in `/app`. `rg` is unavailable (`/bin/bash: rg: command not found`); using local grep/find. No code fix attempted yet.

## Root cause and hypothesis

`Request.open` returns `urllib_request.urlopen` unchanged, so consumers read compressed wire bytes. `fetch_url` only copies response headers into `info`; `uri` and `get_url` both consume the raw returned stream. The existing header normalization in `fetch_url` must be retained. A regression test in `test_gzip_response.py` fails in all four variants with `TypeError: Request.open() got an unexpected keyword argument 'decompress'` (command: `PYTHONPATH=lib pytest -q test/units/module_utils/urls/test_gzip_response.py`). Hypothesis: wrapping only gzip encoded responses in a reader backed by `gzip.GzipFile` will decode the stream while preserving response metadata and opt out behavior.

## Implementation and verification

Added `GzipDecodedReader`, gzip negotiation and stream wrapping in `Request.open`, instance/default propagation through URL helpers, and `decompress` module options for `uri` and `get_url`. Kept response metadata available through the wrapper and retained lowercase `fetch_url` info headers. Missing gzip causes direct Request/open_url calls to raise an actionable `MissingModuleError`; `fetch_url` emits `module.deprecate(..., version='2.16')` and disables decompression, as required.

Focused regression tests cover compressed and uncompressed streams, opt out, complete reads beyond compressed Content-Length, explicit Accept-Encoding, instance defaults, lowercase headers, missing gzip, and a Python 2 style file pointer. Existing tests were updated for the new public argument and negotiated header. Final checks: `PYTHONPATH=lib pytest -q -o reruns=0 test/units/module_utils/urls` passed (89 tests); `PYTHONPATH=lib python -m py_compile lib/ansible/module_utils/urls.py lib/ansible/modules/uri.py lib/ansible/modules/get_url.py` passed; `git diff --check` passed. Native Python 2 execution was unavailable; its file pointer branch was exercised with a simulated object under Python 3.
