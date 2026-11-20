Added `destination_ports` to the [iptables module](/app/lib/ansible/modules/iptables.py). It defaults to an empty list and builds a single `-m multiport --dports` rule for the supplied ports or ranges. The module rejects it unless the protocol is tcp, udp, udplite, dccp, or sctp.

Added coverage in [test_iptables.py](/app/test/units/modules/test_iptables.py). All 23 iptables unit tests pass.