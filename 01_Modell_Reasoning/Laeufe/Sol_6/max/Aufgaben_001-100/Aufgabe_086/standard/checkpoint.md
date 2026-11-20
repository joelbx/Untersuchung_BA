# Checkpoint

Task: Add `destination_ports` support to the iptables module with multiport and protocol restrictions.

Status: Complete.

Changes:
- Added the list parameter with an empty default, documentation, and an example.
- Built multiport rules with `append_match` and `append_csv`, avoiding duplicate explicit matches.
- Rejected nonempty destination_ports for protocols other than tcp, udp, udplite, dccp, and sctp.
- Added focused unit tests and a changelog fragment.

Verification:
- `PYTHONPATH=lib pytest -q test/units/modules/test_iptables.py`: 25 passed.
- `git diff --check`: passed.
