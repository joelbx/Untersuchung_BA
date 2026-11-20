Task: add destination_ports multiport support to the iptables module.
Status: implemented and verified.
Changes: documented the list parameter with empty default and example; render -m multiport --dports with append_match and append_csv; validate allowed protocols; added unit coverage for rendering and rejected protocols.
Verification: PYTHONPATH=lib:test python -m pytest -q test/units/modules/test_iptables.py (23 passed); git diff --check passed.
