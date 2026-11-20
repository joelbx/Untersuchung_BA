Correction round: inspecting current patch and review of PyOpenSSL client-cert/Unix-socket cipher handling.
Confirmed: fallback HTTPSClientAuthHandler drops context for client-cert and Unix-socket connections. Fixing its connection builder and adding regression coverage.
Fixed: HTTPSClientAuthHandler now passes the configured fallback context to client-cert and Unix HTTPS connections; Unix TLS wrapping uses that context. Added mocked fallback regression tests.
Validation: python -m pytest -q test/units/module_utils/urls test/units/plugins/lookup/test_url.py -> 136 passed, 4 warnings. git diff --check clean.
TEST_ENVIRONMENT_PROBLEM: real PyOpenSSL fallback cannot run locally because OpenSSL is unavailable; mocked-context coverage passes.
