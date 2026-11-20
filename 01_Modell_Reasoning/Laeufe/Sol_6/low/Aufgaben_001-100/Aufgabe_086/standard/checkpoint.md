Task: add iptables destination_ports multiport support.
Status: implemented and verified.
Test: PYTHONPATH=/app/lib:/app/test python -m pytest -q test/units/modules/test_iptables.py (23 passed).
