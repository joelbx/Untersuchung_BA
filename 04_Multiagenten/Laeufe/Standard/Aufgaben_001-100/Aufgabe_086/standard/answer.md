Added `destination_ports` to the iptables module with an empty-list default. A nonempty list produces a single `-m multiport --dports` rule and is accepted only with tcp, udp, udplite, dccp, or sctp. The module documentation and example are updated.

Verification: all 23 iptables unit tests pass; `git diff --check` passes.