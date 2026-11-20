Implemented configurable TLS ciphers across [`Request`, `open_url`, `fetch_url`, `get_url`, `uri`, and the URL lookup](/app/lib/ansible/module_utils/urls.py:611). The shared context applies cipher lists or OpenSSL strings to HTTPS requests, redirects, proxies, and Unix socket connections. Invalid cipher settings produce sanitized errors, and disabled certificate validation still excludes SSLv2 and SSLv3.

Added the public CA discovery helper [`get_ca_certs`](/app/lib/ansible/module_utils/urls.py:534) and documented the new option in the modules and lookup. Unset ciphers are forwarded explicitly as `None`.

Verification: **120 URL and lookup unit tests passed**. Compilation, `ansible-doc` loading, context smoke checks, and `git diff --check` also passed.