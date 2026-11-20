Goal: Add custom TLS ciphers across get_url, uri, url lookup, and shared URL helpers.
Status: Implemented and verified locally. Existing URL unit suite: 124 passed.
Changes: Public get_ca_certs/make_context, ciphers propagation and validation, redirect/proxy/Unix socket context wiring, docs and focused unit tests.
Delegation: None; solution implemented directly.
Constraints: local code/tests only; defaults preserved; explicit ciphers=None propagation.
