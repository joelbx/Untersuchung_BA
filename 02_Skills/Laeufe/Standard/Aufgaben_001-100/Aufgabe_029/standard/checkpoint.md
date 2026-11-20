# Checkpoint

Task: Add an idempotent NIOS fixed address module for IPv4 and IPv6 and update API object handling.

Implemented:
- Added `nios_fixed_address.py` with required name, IP, MAC, network, and provider; optional network view, DHCP options, extensible attributes, and comment; present/absent and check mode.
- Address validation selects the WAPI object type and renames `ipaddr` to the corresponding WAPI field after collecting lookup fields.
- Added fixed address object constants and an explicit MAC/address/network/view lookup path in `get_object_ref`.
- Added unit tests for IPv4 and IPv6 creation, lookup, idempotence, update, check mode deletion, invalid addresses, and DHCP option sanitization.

Checks:
- `PYTHONPATH=lib:test python -m pytest -q test/units/modules/net_tools/nios test/units/module_utils/net_tools/nios`: 70 passed.
- `PYTHONPATH=lib:test python -m py_compile lib/ansible/modules/net_tools/nios/nios_fixed_address.py lib/ansible/module_utils/net_tools/nios/api.py`: passed.
- `git diff --check`: passed.

Tooling: `rg` unavailable (`/bin/bash: rg: command not found`); used `find` and `grep` for repository search.
