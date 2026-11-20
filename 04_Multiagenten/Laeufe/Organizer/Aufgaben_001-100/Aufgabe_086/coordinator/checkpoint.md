# Iptables destination_ports checkpoint

- Task: add a `destination_ports` list with an empty default, rendered through iptables multiport for supported protocols.
- Implemented argument, documentation, rule construction, protocol validation, and focused unit coverage.
- Focused test suite passed with `PYTHONPATH=/app/lib:/app/test python -m pytest -q test/units/modules/test_iptables.py` before the final integer input refinement.
- No delegation used.
