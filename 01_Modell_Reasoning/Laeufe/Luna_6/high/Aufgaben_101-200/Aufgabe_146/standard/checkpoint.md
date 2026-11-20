# Checkpoint

Implemented `LinuxHardware.get_sysinfo_facts()` in `lib/ansible/module_utils/facts/hardware/linux.py`.

- Returns `{}` if `/proc/sysinfo` is absent.
- When present, returns exactly `system_vendor`, `product_name`, `product_serial`, `product_version`, and `product_uuid`, defaulting undiscovered values to `NA`.
- Parses `Manufacturer:`, `Type:`, and `Sequence Code:`; strips leading zeros from the serial.
- `get_dmi_facts()` fills unavailable DMI values from sysinfo.

Validation: `python -m pytest test/units/module_utils/facts/hardware/test_linux.py -q` passed (11 tests). `git diff --check` passed.
