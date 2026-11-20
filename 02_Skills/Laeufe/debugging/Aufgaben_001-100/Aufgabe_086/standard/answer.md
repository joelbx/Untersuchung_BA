Added `destination_ports` to the [iptables module](/app/lib/ansible/modules/iptables.py). It defaults to an empty list and builds a single rule using `-m multiport --dports` for ports and ranges. Nonempty lists are accepted only with tcp, udp, udplite, dccp, or sctp. Documentation and unit tests were updated.

Verification: all 24 iptables unit tests passed; `git diff --check` passed.