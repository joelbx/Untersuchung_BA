VERDICT: FIX

**Code defect:** In the PyOpenSSL fallback path, requests using a client certificate or Unix socket select `HTTPSClientAuthHandler`, but [Request.open](/app/lib/ansible/module_utils/urls.py:1523) does not give that handler the configured cipher context. Its [connection builder](/app/lib/ansible/module_utils/urls.py:606) therefore cannot apply the requested ciphers. Route these requests through a connection that uses the context created by `make_context`.

**Tests:** `python -m pytest -q test/units/module_utils/urls test/units/plugins/lookup/test_url.py` — 134 passed, 4 warnings.

**TEST_ENVIRONMENT_PROBLEM:** The real PyOpenSSL fallback could not be exercised locally because `OpenSSL` is unavailable. The passing tests do not cover this path.