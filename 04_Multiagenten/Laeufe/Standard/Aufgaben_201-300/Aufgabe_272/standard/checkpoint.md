Task: Support custom TLS ciphers in get_url, uri, URL lookup, and URL utility layers.
Status: Implemented and verified. Public make_context/get_ca_certs helpers added; ciphers are validated and passed explicitly through fetch_url, open_url, and Request. Context is shared by HTTPS handlers for direct requests, redirects, proxies, Unix sockets, and client certificates. User documentation updated.
Tests: 133 passed in test/units/module_utils/urls and test/units/plugins/lookup/test_url.py; git diff --check clean.
