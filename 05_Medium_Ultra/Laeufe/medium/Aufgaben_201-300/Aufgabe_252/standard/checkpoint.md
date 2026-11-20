Task: fix BSD gather_facts uptime and robust sysctl parsing.
Status: implementation and tests complete. Added uptime collection through `sysctl -n kern.boottime` for FreeBSD, NetBSD, and OpenBSD; hardened shared sysctl parsing, warnings, and multiline handling. Added focused unit coverage.
Verification: PYTHONPATH=/app/lib:/app/test python -m pytest -q test/units/module_utils/facts/test_sysctl.py test/units/module_utils/facts/hardware test/units/module_utils/facts/network/test_generic_bsd.py (31 passed); git diff --check passed.
Constraints honored: local code/tests only; no git history, index, or harness changes.
