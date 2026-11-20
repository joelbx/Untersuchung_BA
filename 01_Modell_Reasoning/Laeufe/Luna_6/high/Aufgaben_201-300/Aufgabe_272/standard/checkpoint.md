# Checkpoint

Implemented configurable TLS ciphers for `get_url`, `uri`, `lookup('url')`, and the shared request stack. Added public `make_context` and `get_ca_certs` helpers, cipher normalization/validation, and propagation through `fetch_url`, `open_url`, `Request`, proxy validation, redirect handling, and Unix socket HTTPS.

Certificate verification remains enabled by default. With verification disabled, the created SSL context excludes SSLv2 and SSLv3. Missing ciphers are explicitly forwarded as `None`.

Validation: Python compilation and `git diff --check` pass. The existing URL utility and URL lookup tests pass when excluding three old call assertions that expect `ciphers` to be omitted; those assertions conflict with the requested explicit `None` forwarding. The other 108 tests pass.
