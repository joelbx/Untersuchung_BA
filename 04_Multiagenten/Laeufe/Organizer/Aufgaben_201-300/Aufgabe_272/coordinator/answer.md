Added custom TLS cipher support to `get_url`, `uri`, and `lookup('url')`. The option accepts an OpenSSL cipher string or an ordered list and passes through `fetch_url`, `open_url`, and `Request`. The shared TLS context applies it to direct HTTPS requests, redirects, proxies, and Unix sockets; invalid values produce clear errors. Calls without a cipher setting explicitly pass `ciphers=None`.

The relevant URL tests passed: **124 passed**. `git diff --check` passed. Testing ran on Python 3.11; Python 3.10 with OpenSSL 1.1.1 was unavailable locally.

No delegation was used; I implemented the changes directly.