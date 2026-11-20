# Checkpoint

Issue: Add configurable TLS ciphers to URL request paths (`get_url`, `uri`, and `lookup('url')`) through shared URL utilities while preserving defaults and validation behavior.

Plan: Inspect `urls.py` and the three public callers, map existing SSL context creation and redirect/proxy/socket paths, implement shared context/cipher configuration, then run the existing relevant unit tests.
