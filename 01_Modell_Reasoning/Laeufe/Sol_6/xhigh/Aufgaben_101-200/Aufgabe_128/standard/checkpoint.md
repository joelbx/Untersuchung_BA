# iptables ipset support checkpoint

- Task: add `match_set` and `match_set_flags` to the iptables module, enforce paired use, and verify rule construction with existing tests.
- Status: implemented parameter validation, set match construction, documentation, and unit coverage.
- Verification: `python -m pytest -q test/units/modules/test_iptables.py` (25 passed); `git diff --check` clean.
