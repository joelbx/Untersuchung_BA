Task: Add ipset set-extension support to Ansible iptables module.
Status: Implemented match_set and match_set_flags with required-together validation and exact flag choices. Rule construction emits -m set --match-set next to explicit set matches or adds the match automatically; leading ! inverts the set test. Added documentation, example, changelog, and unit coverage for explicit/implicit matches, inversion, choices, validation, and command order.
Verification: python -m pytest -q test/units/modules/test_iptables.py (25 passed); git diff --check passed.
Constraints observed: Used local repository only; did not change git history, index baseline, or harness configuration.
