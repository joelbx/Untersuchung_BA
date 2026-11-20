Task: Add configurable TLS ciphers for get_url, uri, url lookup, and shared URL helpers.
Status: implementation complete.
Changed: public make_context/get_ca_certs helpers; ciphers propagated through Request, open_url, fetch_url and module/lookup entry points; consistent HTTPS contexts for redirects, proxies, and Unix sockets; sanitized invalid-cipher errors; documentation and focused tests.
Verification: 126 URL utility and URL lookup unit tests passed; compileall and git diff --check passed.
