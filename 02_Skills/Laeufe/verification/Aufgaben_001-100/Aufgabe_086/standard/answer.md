Added `destination_ports` to the iptables module. It accepts a list of ports and ranges, defaults to an empty list, generates a single `-m multiport --dports` rule, and requires tcp, udp, udplite, dccp, or sctp.

Added documentation and unit tests. Verification: 23 iptables tests passed with `PYTHONPATH=lib:test`; `git diff --check` passed. No live iptables rule was applied.