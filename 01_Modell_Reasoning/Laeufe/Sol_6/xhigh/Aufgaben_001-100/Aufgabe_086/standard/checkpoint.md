Task: add destination_ports support to the iptables module.
Status: implemented destination_ports with multiport command generation, protocol validation, documentation, changelog, and unit coverage.
Verification: PYTHONPATH=/app/lib:/app/test python -m pytest -q test/units/modules/test_iptables.py (24 passed); git diff --check (passed).
