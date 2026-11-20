# Checkpoint

Issue: add ipset set-extension support to the iptables module.
Status: implemented and verified.
Changes: match_set and match_set_flags arguments, required-together validation, rule construction with explicit set extension and inversion, docs/example, unit tests, changelog.
Verification: python -m pytest -q test/units/modules/test_iptables.py (25 passed); git diff --check (passed).
Delegation: none.
