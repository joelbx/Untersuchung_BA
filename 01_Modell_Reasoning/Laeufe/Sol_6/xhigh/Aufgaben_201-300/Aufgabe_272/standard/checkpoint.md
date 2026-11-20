# TLS cipher support checkpoint

Status: implementation complete.

Changes: exposed `ciphers` for get_url, uri, and url lookup; forwarded explicit `None` or user values through fetch_url, open_url, and Request; added public `get_ca_certs` and `make_context`; applied the configured context to direct HTTPS, HTTP-to-HTTPS redirects, proxy tunnels, and Unix HTTPS sockets. Invalid cipher configurations produce clear errors without echoing the supplied value.

Verification: `PYTHONPATH=lib:test pytest -q --override-ini='addopts=' test/units/module_utils/urls test/units/plugins/lookup/test_url.py` passed (138 tests). `git diff --check` passed.
