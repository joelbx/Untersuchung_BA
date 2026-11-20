# Checkpoint

Task: Add `destination_ports` support to the iptables Ansible module using the multiport match, restricted to tcp, udp, udplite, dccp, and sctp.

Implemented:
- Added the documented `destination_ports` list parameter with an empty-list default.
- Added multiport rule construction through `append_match` and `append_csv` (`-m multiport --dports ...`).
- Rejects nonempty destination port lists unless one of the supported protocols is specified.
- Added a module example, changelog fragment, and unit coverage for the supported protocols, ranges, and invalid protocol cases.

Verification:
- `PYTHONPATH=lib pytest -q test/units/modules/test_iptables.py`: 23 passed.
- `git diff --check`: passed.
- `ansible-test units --python 3.9 test/units/modules/test_iptables.py` ran against a stale module copy lacking the changed argument; the direct pytest run with the checked-out `lib` source passed.
