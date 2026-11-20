Added `destination_ports` to the [iptables module](/app/lib/ansible/modules/iptables.py). It defaults to an empty list and builds a single `-m multiport --dports` rule for ports and ranges. The module accepts it only with tcp, udp, udplite, dccp, or sctp.

Added [unit tests](/app/test/units/modules/test_iptables.py) and a usage example. All 23 iptables unit tests pass; `git diff --check` passes.