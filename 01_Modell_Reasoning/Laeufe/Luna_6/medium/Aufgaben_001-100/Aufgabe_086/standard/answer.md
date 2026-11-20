Added `destination_ports` as a list with an empty default. Rules with ports now use the `multiport` match and comma-separated destination ports; a nonempty list requires `tcp`, `udp`, `udplite`, `dccp`, or `sctp`. Added a changelog fragment.

The existing iptables unit suite passed: **21 tests**.