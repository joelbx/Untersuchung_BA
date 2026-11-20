# Checkpoint

Task: add `destination_ports` list support to the iptables module using multiport for tcp, udp, udplite, dccp, and sctp.

Implemented in `lib/ansible/modules/iptables.py`: documented list parameter with empty-list default; construction via `append_match` and `append_csv`; rejection of unsupported or absent protocols. Added a usage example and unit coverage in `test/units/modules/test_iptables.py` for all five protocols, mixed port and range values, and rejected protocols.

Verification:
- `python -m pytest -q test/units/modules/test_iptables.py` exited 1: 2 new tests failed because Python imported `/usr/local/lib/python3.9/dist-packages/ansible/modules/iptables.py` instead of the checkout. This is an invocation path issue, not a repository test result.
- `PYTHONPATH=lib:test python -m pytest -q test/units/modules/test_iptables.py` exited 0: 23 passed.
- `git diff --check` exited 0.

No live iptables command was executed; tests mock `run_command` and verify the generated argv.
