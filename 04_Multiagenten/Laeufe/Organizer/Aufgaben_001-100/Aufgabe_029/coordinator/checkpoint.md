Task: implement nios_fixed_address for IPv4/IPv6 and update NIOS API lookup.
Status: complete. Added fixed address module, WAPI constants and MAC/address/network/view lookup handling, option removal detection, and focused unit tests.
Verification: PYTHONPATH=lib:test python -m pytest -q test/units/modules/net_tools/nios test/units/module_utils/net_tools/nios (69 passed). git diff --check passed.
Delegation: none.
