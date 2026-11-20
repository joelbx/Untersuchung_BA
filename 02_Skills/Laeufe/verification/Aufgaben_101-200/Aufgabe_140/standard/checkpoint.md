# Checkpoint

Task: fix hosts blocking for parent domains, whitelist precedence, and hostname widening.
Status: implementation and focused verification complete.

Changes: added urlutils.widened_hostnames, checked parent domains in both host sets after the blocking toggle and whitelist, and normalized trailing dots during matching. Added unit coverage for widening, parent domains, both sets, whitelist, and toggle behavior. Corrected a per-URL test fixture to use an absolute URL with a real host.

Verification: `QT_QPA_PLATFORM=offscreen python -m pytest -q tests/unit/components/test_hostblock.py tests/unit/utils/test_urlutils.py` exited 0 (357 passed, 1 skipped). `git diff --check` exited 0.
