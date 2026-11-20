Implemented `nios_fixed_address` for IPv4 and IPv6, including required parameters, DHCP options, metadata, check mode, and MAC based lookup. Added the Fixed Address API constants and lookup support in [api.py](/app/lib/ansible/module_utils/net_tools/nios/api.py).

Validation: all 63 existing NIOS unit tests passed; helper checks, `py_compile`, and `git diff --check` passed.