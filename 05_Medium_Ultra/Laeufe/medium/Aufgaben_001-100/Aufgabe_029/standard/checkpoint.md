Task: implement NIOS DHCP fixed address module for IPv4/IPv6 and API support.
Status: completed repository edits and local verification.
Changes: added nios_fixed_address module with required provider/name/ipaddr/mac/network, address validation and WAPI remapping, DHCP options, metadata, state handling via WapiModule; added fixed address constants and MAC-based lookup in API; added focused unit tests.
Verification: PYTHONPATH=lib:test python -m pytest -q test/units/modules/net_tools/nios test/units/module_utils/net_tools/nios (68 passed); python -m py_compile for changed Python modules; git diff --check.
