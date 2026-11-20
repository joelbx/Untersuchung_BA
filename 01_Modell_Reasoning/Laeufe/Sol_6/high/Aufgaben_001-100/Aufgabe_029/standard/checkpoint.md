Task: add NIOS fixed address management for IPv4 and IPv6.

Status: implemented nios_fixed_address for IPv4/IPv6 with address validation, required provider, DHCP options, metadata, state handling, and check mode. Added fixed-address constants and MAC/address/network lookup support in the WAPI helper. Added focused unit tests.

Verification: 72 NIOS unit tests passed with `PYTHONPATH=lib:test python -m pytest -q test/units/modules/net_tools/nios test/units/module_utils/net_tools/nios`. `git diff --check` and Python compilation passed.
