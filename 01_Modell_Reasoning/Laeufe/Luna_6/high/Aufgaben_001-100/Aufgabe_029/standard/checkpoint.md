# Checkpoint

Implemented `nios_fixed_address.py` with IPv4/IPv6 validation and WAPI address field mapping, MAC/network identity filtering, DHCP option sanitization, metadata, default state, and check mode support. Added both Fixed Address object constants and MAC based lookup handling to the NIOS API helper.

Validation completed:
- Full existing NIOS module and API unit test suites: 63 passed.
- Direct helper checks: IPv4 and IPv6 object selection/remapping and DHCP option `None` filtering passed.
- `py_compile` and `git diff --check` passed.

`rg` is unavailable in this environment; repository discovery used `find` and file reads instead.
