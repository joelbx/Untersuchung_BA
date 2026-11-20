Task: Add iptables `destination_ports` list support using multiport for tcp, udp, udplite, dccp, and sctp.

Status: Implemented documented `destination_ports` list with an empty default, multiport command construction, and protocol validation. Added unit coverage for all supported protocols and unsupported protocols.

Verification: `PYTHONPATH=lib:test python -m pytest -q test/units/modules/test_iptables.py` passed (23 tests). `git diff --check` passed.
