# Checkpoint

Implemented `destination_ports` in `lib/ansible/modules/iptables.py`: list of strings with an empty-list default, emitted using `append_match(..., 'multiport')` and `append_csv(..., '--destination-ports')`. The module rejects nonempty values unless protocol is tcp, udp, udplite, dccp, or sctp. Added module documentation and a usage example.

Added unit coverage for CSV rule construction and unsupported-protocol validation in `test/units/modules/test_iptables.py`.

Verification: `PYTHONPATH=/app/lib python -m pytest test/units/modules/test_iptables.py` passed (23 tests); `git diff --check` passed. `bin/ansible-test units ...` could not run because the selected Python 3.8 environment lacks pytest. Direct pytest without `PYTHONPATH` loads the installed module and is not representative.
