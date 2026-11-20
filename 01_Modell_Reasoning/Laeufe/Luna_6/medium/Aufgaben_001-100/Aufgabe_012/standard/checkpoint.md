# Checkpoint

Issue: preserve JavaScript XHR `Accept-Language` headers from global fallback while honoring per-domain overrides.

Plan: locate `custom_headers` and `interceptRequest`, inspect existing focused tests, make the smallest compatible change, and run relevant repository tests.
