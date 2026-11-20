Task: add ipset set-extension support to the Ansible iptables module.
Status: complete.
Changes: documented match_set and match_set_flags; added paired-parameter and flag-choice validation; generated one set extension clause with standard inversion; added unit coverage for all flag choices, explicit/implicit set match, inversion, add-rule path, and invalid inputs.
Verification: python -m pytest -q test/units/modules/test_iptables.py (26 passed); git diff --check passed.
