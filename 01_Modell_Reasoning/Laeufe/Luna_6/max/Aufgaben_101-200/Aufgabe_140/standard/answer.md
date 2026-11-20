Implemented host blocking across the request hostname and its parent domains, with early exits for disabled blocking and whitelisted URLs. Trailing dots now match either way, and `urlutils.widened_hostnames` provides the requested widening behavior.

Updated the per URL toggle test to use a full URL so it exercises a real hostname.

Validation: 347 passed, 1 skipped across the URL utility and host blocker suites.

Files: [hostblock.py](/app/qutebrowser/components/hostblock.py:114), [urlutils.py](/app/qutebrowser/utils/urlutils.py:430), [test_hostblock.py](/app/tests/unit/components/test_hostblock.py:279).