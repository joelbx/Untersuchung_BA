# Checkpoint

Implemented custom TLS ciphers for `get_url`, `uri`, and `lookup('url')` through `fetch_url`, `open_url`, `Request`, and shared `make_context`/`get_ca_certs` interfaces. Cipher settings are applied to the HTTPS handler used by direct requests, HTTP-to-HTTPS redirects, proxies, and Unix socket connections on the native SSLContext path. Invalid cipher input raises a safe, user-facing error. Defaults continue to pass `ciphers=None` explicitly.

Verification:
- `PYTHONPATH=lib python -m pytest -q test/units/module_utils/urls test/units/plugins/lookup/test_url.py` — 131 passed, 3 existing deprecation warnings.
- `python -m compileall -q lib/ansible/module_utils/urls.py lib/ansible/modules/get_url.py lib/ansible/modules/uri.py lib/ansible/plugins/lookup/url.py test/units/module_utils/urls/test_ciphers.py && git diff --check` — passed.

Environment limits: Python here is 3.11.13, so the stated Python 3.10/OpenSSL 1.1.1 combination was not exercised. Optional PyOpenSSL is absent: `python - <<'PY'\nfrom urllib3.contrib.pyopenssl import PyOpenSSLContext\nimport inspect\nprint(inspect.getsource(PyOpenSSLContext.options.fset))\nPY` failed with `ModuleNotFoundError: No module named 'OpenSSL'`; PyOpenSSL behavior is supported by code but remains unverified here. No dependencies were downloaded.

`rg` is unavailable (`/bin/bash: rg: command not found`); local search used grep/find.
