Implemented the fixed address module in [nios_fixed_address.py](/app/lib/ansible/modules/net_tools/nios/nios_fixed_address.py). It supports IPv4 and IPv6, present/absent states, check mode, metadata, and validated DHCP options.

Updated [api.py](/app/lib/ansible/module_utils/net_tools/nios/api.py) with both fixed address object constants and lookup handling by MAC, network, and address family.

Verification: the existing NIOS unit suite passed, **54 tests**. `git diff --check` passed.