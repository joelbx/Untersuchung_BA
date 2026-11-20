Task: Add configurable TLS ciphers to get_url, uri, lookup('url'), and shared URL utilities.
Status: Completed repository edits.
Changes: Added public make_context/get_ca_certs; propagated ciphers (including explicit None) through URL modules, lookup, fetch_url, open_url, Request, redirect, proxy, and Unix socket handlers; added static invalid-cipher errors and documentation.
Verification: PYTHONPATH=lib pytest -q test/units/module_utils/urls test/units/plugins/lookup/test_url.py — 135 passed. git diff --check passed.
Environment: Tests ran on Python 3.11; no CentOS 7 / Python 3.10 / OpenSSL 1.1.1 runtime available locally.
