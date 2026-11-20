# Checkpoint

Task: Add `destination_ports` support to the Ansible iptables module using the multiport match helpers and restrict nonempty values to tcp, udp, udplite, dccp, and sctp.

Completed:
- Added the list parameter with an empty-list default, documentation, example, and protocol validation.
- Generated `-m multiport --dports` through `append_match` and `append_csv`.
- Added a minor changes fragment.
- Ran `python -m pytest -q test/units/modules/test_iptables.py`: 21 passed.
- `git diff --check` passed.
