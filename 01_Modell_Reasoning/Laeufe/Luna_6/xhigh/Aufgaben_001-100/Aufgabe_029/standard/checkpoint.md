# Work checkpoint

Issue: add Ansible support for Infoblox DHCP fixed addresses (IPv4 and IPv6), with idempotent state management, DHCP options, extattrs, comments, check mode, and MAC-based lookup support.

Inspection findings:
- NIOS modules use `WapiModule.run()` for present/absent state and the shared NIOS provider spec.
- `nios_network.py` provides the DHCP option schema and the existing IPv4/IPv6 validators.
- `WapiModule.run()` creates its lookup filter from `ib_req` fields; fixed address needs that filter captured before `ipaddr` is renamed to the WAPI address field.
- No fixed-address unit test currently exists. Existing NIOS module tests are available for regression coverage.

Implementation complete:
- Added `nios_fixed_address.py` with IPv4/IPv6 address selection, required provider and identity fields, state/check-mode support, comments, extattrs, and DHCP option sanitization/defaults.
- Added fixed-address WAPI constants and explicit MAC-aware lookup handling in `api.py`. `WapiModule.run()` accepts a prebuilt lookup filter while preserving existing callers.

Verification:
- All 54 existing NIOS unit tests passed with `PYTHONPATH=lib:test python3 -m pytest -q test/units/modules/net_tools/nios`.
- `python -m py_compile` passed for the changed Python files, and `git diff --check` passed.
- `ansible-test` could not run because this environment lacks the Python 2.6 and Python 3.7 interpreters it requires; pytest on the available Python 3.11 completed the test suite.
