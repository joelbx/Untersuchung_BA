Task: Implement NIOS fixed address module for IPv4/IPv6 and update API constants/reference handling.
Status: Complete. Added nios_fixed_address.py, fixed address constants and MAC/address/network lookup handling, plus focused unit tests.
Verification: python -m pytest -q test/units/modules/net_tools/nios (58 passed); git diff --check passed.
Constraints observed: Used local code and tests only; did not alter git history, index baseline, or harness configuration.
