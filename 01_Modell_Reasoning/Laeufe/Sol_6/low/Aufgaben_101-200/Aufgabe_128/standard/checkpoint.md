Task: Add ipset set-extension support to the iptables module.
Status: Implemented match_set/match_set_flags with pair validation, automatic set match, inversion, documentation, and unit tests.
Verification: python -m pytest -q test/units/modules/test_iptables.py (25 passed); git diff --check passed.
